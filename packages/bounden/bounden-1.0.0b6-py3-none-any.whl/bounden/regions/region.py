from typing import Any, Generic, Optional, cast

from bounden.coordinates import AxesT
from bounden.log import log
from bounden.points import Point
from bounden.protocols import RegionProtocol
from bounden.vectors import Vector
from bounden.volumes import Length, LengthsT, Volume


class Region(RegionProtocol, Generic[AxesT, LengthsT]):
    """
    A region of n-dimensional space.

    `position` describes the region's origin. Must be relative if a parent
    region is set, otherwise absolute.

    `volume` describes the region's size.
    """

    def __init__(
        self,
        position: AxesT | Point[AxesT],
        volume: LengthsT | Volume[LengthsT],
        parent: Optional[RegionProtocol] = None,
    ) -> None:
        if len(position) != len(volume):
            raise ValueError(
                f"Coordinates count ({len(position)}) "
                f"!= lengths count ({len(volume)})"
            )

        self._parent = parent

        if isinstance(position, Point):
            self._position = position
        else:
            self._position = Point[AxesT](position)

        if isinstance(volume, Volume):
            self._volume = volume
        else:
            self._volume = Volume[LengthsT](volume)

    def __add__(self, other: Any) -> "Region[AxesT, LengthsT]":
        if isinstance(other, Vector):
            vector: Vector[Any] = other
            region = Region[AxesT, LengthsT](
                self.position + other,
                self.volume,
                parent=self._parent,
            )
            log.debug("Vector %s + region %s == %s", vector, self, region)
            return region

        raise ValueError(
            f"Cannot add {repr(other)} ({other.__class__.__name__}) to "
            f"{self.__class__.__name__}"
        )

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Region):
            o: Region[Any, Any] = other
            return self.position == o.position and self.volume == o.volume

        return False

    def __repr__(self) -> str:
        return f"{self.position} x {self.volume}"

    @property
    def absolute(self) -> "Region[AxesT, LengthsT]":
        """
        Copy of this region with absolute coordinates.
        """

        if self._parent:
            return self + self._parent.absolute.position.vector

        return self

    @property
    def center(self) -> Point[AxesT]:
        """
        Center.
        """

        cl = [self._position[i] + (l / 2) for i, l in enumerate(self.volume)]
        return self._position.__class__(cast(AxesT, tuple(cl)))

    def expand(self, distance: Length) -> "Region[AxesT, LengthsT]":
        """
        Gets a copy of this region expanded by `distance` about its centre.

        Pass a negative distance to contract.
        """

        position = self.position - (distance / 2)
        volume = self.volume.expand(distance)
        return self.__class__(position, volume)

    def point(self, coordinates: AxesT) -> Point[AxesT]:
        """
        Creates a child point.
        """

        return self._position.__class__(coordinates, parent=self)

    @property
    def position(self) -> Point[AxesT]:
        """
        Position.
        """

        return self._position

    @property
    def volume(self) -> Volume[LengthsT]:
        """
        Volume.
        """

        return self._volume
