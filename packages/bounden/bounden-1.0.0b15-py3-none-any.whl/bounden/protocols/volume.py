from typing import Protocol


class VolumeProtocol(Protocol):
    """
    Volume protocol.
    """

    def absolute(self, dimension: int) -> float:
        """
        Gets the absolute length of `dimension`.
        """
