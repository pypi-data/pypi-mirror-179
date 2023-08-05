from typing import Protocol

from bounden.protocols.vector import VectorProtocol


class PointProtocol(Protocol):
    """
    Point protocol.
    """

    @property
    def vector(self) -> VectorProtocol:
        """
        Coordinates as a vector.
        """
