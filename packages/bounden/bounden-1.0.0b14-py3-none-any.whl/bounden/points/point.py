from typing import Any, Generic, Optional, TypeVar, cast

from bounden.coordinates import AxesT, Coordinate
from bounden.protocols import PointProtocol, RegionProtocol
from bounden.vectors import Vector


class Point(PointProtocol, Generic[AxesT]):
    """
    A point in n-dimensional space.
    """

    def __init__(
        self,
        coordinates: AxesT,
        parent: Optional[RegionProtocol] = None,
    ) -> None:
        self._coordinates = coordinates
        self._parent = parent

    def __add__(self, other: Any) -> "Point[AxesT]":
        if isinstance(other, Vector):
            v: Vector[Any] = other

            if len(v) != len(self):
                raise ValueError(
                    f"Vector force count ({len(v)}) != "
                    f"point dimension count ({len(self)})"
                )

            cl = [c + v[i] for i, c in enumerate(self.coordinates)]
            return Point[AxesT](cast(AxesT, tuple(cl)), parent=self._parent)

        if isinstance(other, (float, int)):
            cl = [c + other for c in self.coordinates]
            return Point[AxesT](cast(AxesT, tuple(cl)), parent=self._parent)

        raise ValueError(
            f"Cannot add {repr(other)} ({other.__class__.__name__}) to "
            f"{self.__class__.__name__}"
        )

    def __getitem__(self, index: int) -> Coordinate[Any]:
        return self.coordinates[index]

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Point):
            o: Point[Any] = other
            return bool(self.coordinates == o.coordinates)

        return bool(self.coordinates == other)

    def __len__(self) -> int:
        return len(self._coordinates)

    def __repr__(self) -> str:
        return str(self._coordinates)

    def __sub__(self, other: Any) -> "Point[AxesT]":
        return self.__add__(other * -1)

    @property
    def absolute(self) -> "Point[AxesT]":
        """
        Copy of this point with absolute coordinates.
        """

        if self._parent:
            return self + self._parent.absolute.position.vector

        return self

    @property
    def coordinates(self) -> AxesT:
        """
        Coordinates.
        """

        return self._coordinates

    @property
    def vector(self) -> Vector[Any]:
        """
        Coordinates as a vector.
        """

        return Vector(tuple(float(c) for c in self.coordinates))


PointT = TypeVar("PointT", bound=Point[Any])
