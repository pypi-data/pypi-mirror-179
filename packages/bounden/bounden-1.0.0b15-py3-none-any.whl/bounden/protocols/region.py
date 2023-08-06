from typing import Protocol

from bounden.protocols.point import PointProtocol
from bounden.protocols.volume import VolumeProtocol


class RegionProtocol(Protocol):
    """
    Region protocol.
    """

    @property
    def absolute(self) -> "RegionProtocol":
        """
        Copy of this region with absolute coordinates.
        """

    @property
    def position(self) -> PointProtocol:
        """
        Position.
        """

    @property
    def volume(self) -> VolumeProtocol:
        """
        Volume.
        """
