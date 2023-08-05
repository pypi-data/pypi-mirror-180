from abc import ABC, abstractmethod

from numpy import uint64


class IQuantumSimulator(ABC):
    """Abstract class for interfacing with a quantum simulators that interacts
    with the HAL.
    """

    @abstractmethod
    def accept_command(
        self,
        command: uint64
    ) -> uint64:
        """Performs required logic based on received commands, and returns
        results if command is a measurement.

        Parameters
        ----------
        command : Tuple[uint64, uint64]
            The HAL command to deconstruct and use to perform actions.
            Composed of upper and lower half.

        Returns
        -------
        uint64
            Result of a measurement command.
        """
