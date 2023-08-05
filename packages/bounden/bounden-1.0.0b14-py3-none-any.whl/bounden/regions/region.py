from typing import Any, Generic, Optional, Sequence, TypeVar, cast

from bounden.coordinates import AxesT
from bounden.log import log
from bounden.points import Point
from bounden.protocols import RegionProtocol
from bounden.vectors import Vector
from bounden.volumes import Percent, Volume


class Region(RegionProtocol, Generic[AxesT]):
    """
    A region of n-dimensional space.

    `position` describes the region's origin. Must be relative if a parent
    region is set, otherwise absolute.

    `volume` describes the region's size.
    """

    def __init__(
        self,
        position: AxesT | Point[AxesT],
        volume: Sequence[float | int | Percent],
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

        self._volume = Volume(
            *volume,
            parent=parent.volume if parent else None,
        )

    def __add__(self: "RegionT", other: Any) -> "RegionT":
        if isinstance(other, Vector):
            vector: Vector[Any] = other
            region = self.__class__(
                self.position + other,
                tuple(self.volume),
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
            o: Region[Any] = other
            return self.position == o.position and self.volume == o.volume

        return False

    def __repr__(self) -> str:
        return f"{self.position} x {self.volume}"

    @property
    def absolute(self: "RegionT") -> "RegionT":
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

    def expand(self: "RegionT", distance: float) -> "RegionT":
        """
        Gets a copy of this region expanded by `distance` about its centre.

        Pass a negative distance to contract.
        """

        position = self.position - (distance / 2)
        volume = self.volume.expand(distance)
        return self.__class__(position, tuple(volume), parent=self._parent)

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

    def region(
        self: "RegionT",
        position: AxesT | Point[AxesT],
        volume: Sequence[float | int | Percent],
    ) -> "RegionT":
        """
        Creates a child region.
        """

        return self.__class__(position, volume, parent=self)

    @property
    def volume(self) -> Volume:
        """
        Volume.
        """

        return self._volume


RegionT = TypeVar("RegionT", bound=Region[Any])
