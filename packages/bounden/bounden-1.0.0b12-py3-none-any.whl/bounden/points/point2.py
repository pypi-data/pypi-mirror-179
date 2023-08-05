from typing import Any, Optional, Type, TypeVar

from bounden.coordinates import Coordinate, XAxisT, YAxisT
from bounden.points.point import Point
from bounden.protocols import RegionProtocol


class Point2(Point[tuple[XAxisT, YAxisT]]):
    """
    A point in two-dimensional space.
    """

    @classmethod
    def new(
        cls: Type["Point2T"],
        x: XAxisT,
        y: YAxisT,
        parent: Optional[RegionProtocol] = None,
    ) -> "Point2T":
        """
        Creates a new `Point2`.
        """

        return cls((x, y), parent=parent)

    @property
    def left(self) -> Coordinate[XAxisT]:
        """
        Left.
        """

        return self.x

    @property
    def top(self) -> Coordinate[YAxisT]:
        """
        Top
        """

        return self.y

    @property
    def x(self) -> Coordinate[XAxisT]:
        """
        X coordinate.
        """

        return self.coordinates[0]

    @property
    def y(self) -> Coordinate[YAxisT]:
        """
        Y coordinate.
        """

        return self.coordinates[1]


Point2T = TypeVar("Point2T", bound=Point2[Any, Any])
