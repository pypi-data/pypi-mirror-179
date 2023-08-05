from typing import Any, Optional, Type, TypeVar

from bounden.coordinates import Coordinate, XAxisT, YAxisT
from bounden.points import Point2
from bounden.protocols import RegionProtocol
from bounden.regions import Region
from bounden.volumes import Percent


class Region2(Region[tuple[XAxisT, YAxisT]]):
    """
    A region of two-dimensional space.
    """

    @classmethod
    def new(
        cls: Type["Region2T"],
        x: XAxisT,
        y: YAxisT,
        width: float | int | Percent,
        height: float | int | Percent,
        parent: Optional[RegionProtocol] = None,
    ) -> "Region2T":
        """
        Creates a new `Region2`.
        """

        return cls(Point2.new(x, y), (width, height), parent=parent)

    @property
    def bottom(self) -> Coordinate[YAxisT]:
        """
        Bottom.
        """

        return self.top + self.height

    @property
    def height(self) -> float | int:
        """
        Height.
        """

        return self.volume.absolute(1)

    @property
    def left(self) -> Coordinate[XAxisT]:
        """
        Left.
        """

        return self.x

    def point2(self, x: XAxisT, y: YAxisT) -> Point2[XAxisT, YAxisT]:
        """
        Creates a child point.
        """

        return Point2.new(x, y, parent=self)

    def region2(
        self: "Region2T",
        x: XAxisT,
        y: YAxisT,
        width: float | int | Percent,
        height: float | int | Percent,
    ) -> "Region2T":
        """
        Creates a child region.
        """

        return self.__class__.new(x, y, width, height, parent=self)

    @property
    def right(self) -> Coordinate[XAxisT]:
        """
        Right.
        """

        return self.left + self.width

    @property
    def top(self) -> Coordinate[YAxisT]:
        """
        Top.
        """

        return self.y

    @property
    def width(self) -> float | int:
        """
        Width.
        """

        return self.volume.absolute(0)

    @property
    def x(self) -> Coordinate[XAxisT]:
        """
        X coordinate.
        """

        return self.position.coordinates[0]

    @property
    def y(self) -> Coordinate[YAxisT]:
        """
        Y coordinate.
        """

        return self.position.coordinates[1]


Region2T = TypeVar("Region2T", bound=Region2[Any, Any])
