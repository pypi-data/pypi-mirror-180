import atexit

import numpy as np
from numpy import uint64
from numpy.random import RandomState

from projectq import MainEngine
from projectq.backends import Simulator
from projectq.ops import (All, C, CNOT, DaggeredGate, H, Measure, R,
                          Rx, Ry, Rz, S, SqrtX, Swap, T, X, Y, Z,
                          Rxx, Rzz)
from projectq.ops._basics import BasicGate, BasicRotationGate

from . import IQuantumSimulator
from ..hal._commands import QHALCommand, Opcode
from ..hal._utils import binary_angle_conversion


class SxGate(BasicGate):
    """Gate that consists of consecutive S and X gate
    (pi-rotation with axis in x-y-plane).
    """

    @property
    def matrix(self):
        return np.array([[0, 1], [1j, 0]])

    def __str__(self):
        return "SX"


#: Shortcut (instance of) :class:`projectq.ops.SxGate`
Sx = SxGate()


class SyGate(BasicGate):
    """Gate that consists of consecutive S and Y gate
    (pi-rotation with axis in x-y-plane).
    """

    @property
    def matrix(self):
        return np.array([[0, 1j], [1, 0]])

    def __str__(self):
        return "SY"


#: Shortcut (instance of) :class:`projectq.ops.SyGate`
Sy = SyGate()


class PiXY(BasicRotationGate):
    """Pi-rotation with axis in x-y-plane gate class."""

    @property
    def matrix(self):
        return np.array([[0, -np.sin(self.angle) - 1j * np.cos(self.angle)],
                         [np.sin(self.angle) - 1j * np.cos(self.angle), 0]])


class PiYZ(BasicRotationGate):
    """Pi-rotation with axis in y-z-plane gate class."""

    @property
    def matrix(self):
        return np.array([[np.cos(self.angle), -1j * np.sin(self.angle)],
                         [1j * np.sin(self.angle), -1 * np.cos(self.angle)]])


class PiZX(BasicRotationGate):
    """Pi-rotation with axis in z-x-plane gate class."""

    @property
    def matrix(self):
        return np.array([[np.cos(self.angle), np.sin(self.angle)],
                         [np.sin(self.angle), -1 * np.cos(self.angle)]])


class Pswap(BasicRotationGate):
    """Parameterised swap gate class."""

    @property
    def matrix(self):
        return np.array([[1, 0, 0, 0],
                        [0, 0, np.exp(1j * self.angle), 0],
                        [0, np.exp(1j * self.angle), 0, 0],
                        [0, 0, 0, 1]])


class ProjectqQuantumSimulator(IQuantumSimulator):
    """Concrete ProjectQ implementation of the IQuantumSimulator interface.

    Parameters
    ----------
    register_size: int
        Size of the qubit register.
    seed : int
        Random number generator seed for both the ProjectQ Simulator and
        circuit errors.
    backend
        ProjectQ backend, could use CircuitDrawer for debugging purposes.
    """

    def __init__(self,
                 register_size: int = 16,
                 seed: int = None,
                 backend=Simulator):
        self._engine = None
        self.backend = backend
        self.seed = seed

        # if random numbers are needed to simulate quantum noise use this
        # state in the following way self._random_state.rand()
        self._random_state = RandomState(seed)

        self._qubit_register = None
        self._measured_qubits = []
        self._offset_registers = [0, 0]  # offsets for qubit indexes 0 and 1

        # defaulted to 16 because the bitcode status return
        # has 16 bits assigned for measurement results.
        self._qubit_register_size = register_size

        # assign projectq gate to each opcode
        self._parameterised_gate_dict = {
            Opcode.R: R,
            Opcode.RX: Rx,
            Opcode.RY: Ry,
            Opcode.RZ: Rz,
            Opcode.PIXY: PiXY,
            Opcode.PIYZ: PiYZ,
            Opcode.PIZX: PiZX,
            Opcode.PSWAP: Pswap,
            Opcode.RXX: Rxx,
            Opcode.RZZ: Rzz
        }

        self._constant_gate_dict = {
            # SINGLE
            Opcode.H: H,
            Opcode.S: S,
            Opcode.SQRT_X: SqrtX,
            Opcode.T: T,
            Opcode.X: X,
            Opcode.Y: Y,
            Opcode.Z: Z,
            Opcode.INVT: DaggeredGate(T),
            Opcode.INVS: DaggeredGate(S),
            Opcode.SX: Sx,  # consecutive S and X gate, needed for RC
            Opcode.SY: Sy,  # consecutive S and Y gate, needed for RC
            # DUAL
            Opcode.CNOT: CNOT,
            Opcode.SWAP: Swap
        }
        atexit.register(self.cleanup)

    def __getstate__(self):
        # Copy the object's state from self.__dict__ which contains
        # all our instance attributes. Always use the dict.copy()
        # method to avoid modifying the original state.
        state = self.__dict__.copy()
        # Remove the engine has it generally unpickable.
        del state['_engine']
        return state

    def __setstate__(self, state):
        # Restore instance attributes (i.e., filename and lineno).
        self.__dict__.update(state)
        # Restore the engine
        if self.backend == Simulator and self.seed is not None:
            self._engine = MainEngine(backend=Simulator(rnd_seed=self.seed))
        else:
            self._engine = MainEngine(backend=self.backend())

    def cleanup(self):
        """Release all the qubits that haven't been handled yet."""
        if self._engine is not None:
            if self._qubit_register is not None:
                All(Measure) | self._qubit_register
            self._engine.flush()
            self._engine = None

    def get_offset(self, qubit_index: int):
        return self._offset_registers[qubit_index]

    def apply_gate(self,
                   gate: BasicGate,
                   qubit_index_0: int,
                   qubit_index_1: int = None,
                   parameter_0: float = None,
                   parameter_1: float = None):
        """Receives command information and implements the gate on the
        corresponding qubit.

        Parameters
        ----------
        gate : BasicGate
            ProjectQ gate to be applied.
        qubit_index : int
            Index of qubit for gate to be applied to.
        parameter : float
            Angle of gate if parametrised.
        """
        if self._qubit_register is not None:

            if qubit_index_1 is None:  # single qubit gate
                if parameter_0 is not None:
                    gate(parameter_0) | self._qubit_register[qubit_index_0]
                else:
                    gate | self._qubit_register[qubit_index_0]

            else:  # multi qubit gate
                if parameter_0 is not None:
                    gate(parameter_0) | (
                        self._qubit_register[qubit_index_0],
                        self._qubit_register[qubit_index_1]
                    )
                else:
                    gate | (
                        self._qubit_register[qubit_index_0],
                        self._qubit_register[qubit_index_1]
                    )

            self._engine.flush()

    def _init_engine(self):
        if self._engine is not None:
            raise ValueError("Simulator engine already initialised!")
        if self.backend == Simulator and self.seed is not None:
            self._engine = MainEngine(backend=Simulator(rnd_seed=self.seed))
        else:
            self._engine = MainEngine(backend=self.backend())

    def _init_qureg(self):
        if self._qubit_register is None:
            self._qubit_register = self._engine.allocate_qureg(
                self._qubit_register_size
            )
            self._measured_qubits = []
        else:
            raise ValueError("Qubit register has already been initialised!")

    def accept_command(
        self,
        command: uint64
    ) -> uint64:

        command_qhal = QHALCommand.from_binary(command)
        op, args, qubit_indexes = command_qhal.opcode, command_qhal.args, command_qhal.qubits

        q_index_0 = qubit_indexes[0] + self.get_offset(0)
        q_index_1 = 0
        if len(qubit_indexes) > 1:
            q_index_1 = qubit_indexes[1] + self.get_offset(1)

        for index in qubit_indexes:
            assert index < self._qubit_register_size, \
                f"Qubit index {index} greater than register size " + \
                f"({self._qubit_register_size})!"

        if op == Opcode.START_SESSION:
            self._init_engine()

        elif op == Opcode.STATE_PREPARATION_ALL:
            self._init_qureg()

        elif op == Opcode.STATE_PREPARATION:
            if self._qubit_register is None:
                self._init_qureg()
            elif q_index_0 in self._measured_qubits:
                if int(self._qubit_register[q_index_0]):
                    X | self._qubit_register[q_index_0]
                self._measured_qubits.remove(q_index_0)
            else:
                raise ValueError("Qubit already prepared!")

        elif op == Opcode.END_SESSION:
            self.cleanup()

        elif op == Opcode.QUBIT_MEASURE:

            if q_index_0 in self._measured_qubits:
                raise ValueError("Qubit already measured!")

            # In the ProjectQ simulator we implement this via a rotation and then measurement.
            arg0 = binary_angle_conversion(args[0])
            arg1 = binary_angle_conversion(args[1])
            Rz(-arg1) | self._qubit_register[q_index_0]
            Ry(-arg0) | self._qubit_register[q_index_0]
            Measure | self._qubit_register[q_index_0]
            self._engine.flush()

            measurement = int(self._qubit_register[q_index_0])
            self._measured_qubits.append(q_index_0)

            if len(self._qubit_register) == len(self._measured_qubits):
                self._qubit_register = None

            # QUBIT INDEX [63-52] | OFFSET [51-12] | STATUS [11-7] | PADDING [6-1] | VALUE [0]
            # TODO: add STATUS
            return (
                (qubit_indexes[0] << 52)
                | (self._offset_registers[0] << 12)
                | measurement
            )

        elif op == Opcode.PAGE_SET_QUBIT_0:
            self._offset_registers[0] = qubit_indexes[0]

        elif op == Opcode.PAGE_SET_QUBIT_1:
            self._offset_registers[1] = qubit_indexes[0]

        elif op == Opcode.ID:
            pass

        elif op.has_param():
            if q_index_0 in self._measured_qubits:
                raise ValueError("Qubit requires re-preparation!")

            arg0 = binary_angle_conversion(args[0])
            arg1 = binary_angle_conversion(args[1])
            gate = self._parameterised_gate_dict[op]
            if op.is_dual():
                self.apply_gate(
                    gate,
                    qubit_index_0=q_index_0,
                    qubit_index_1=q_index_1,
                    parameter_0=arg0,
                    parameter_1=arg1
                )
            else:
                self.apply_gate(gate, q_index_0,
                                parameter_0=arg0, parameter_1=arg1)

        elif not op.has_param():
            if q_index_0 in self._measured_qubits:
                raise ValueError("Qubit requires re-preparation!")

            gate = self._constant_gate_dict[op]
            if op.is_dual():
                self.apply_gate(
                    gate,
                    qubit_index_0=q_index_0,
                    qubit_index_1=q_index_1
                )
            else:
                self.apply_gate(gate, q_index_0)
        else:
            raise TypeError(f"{op} is not a recognised opcode!")
