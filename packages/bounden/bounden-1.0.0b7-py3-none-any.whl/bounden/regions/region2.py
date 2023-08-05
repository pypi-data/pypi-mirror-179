from bounden.coordinates import Coordinate, XAxisT, YAxisT
from bounden.points import Point2
from bounden.regions import Region
from bounden.volumes import Volume2
from bounden.volumes.types import XLengthT, YLengthT


class Region2(Region[tuple[XAxisT, YAxisT], tuple[XLengthT, YLengthT]]):
    """
    A region of two-dimensional space.

    `x` and `y` describe the region's origin.

    `width` and `height` describe the region's dimensions.
    """

    @classmethod
    def new(
        cls,
        x: XAxisT,
        y: YAxisT,
        width: XLengthT,
        height: YLengthT,
    ) -> "Region2[XAxisT, YAxisT, XLengthT, YLengthT]":
        """
        Creates a new `Region2`.
        """

        return Region2(Point2.new(x, y), Volume2.new(width, height))

    @property
    def bottom(self) -> Coordinate[YAxisT]:
        """
        Bottom.
        """

        return self.top + self.height

    @property
    def height(self) -> YLengthT:
        """
        Height.
        """

        return self.volume.lengths[1]

    @property
    def left(self) -> XAxisT:
        """
        Left.
        """

        return self.position.coordinates[0]

    def point2(self, x: XAxisT, y: YAxisT) -> Point2[XAxisT, YAxisT]:
        """
        Creates a child point.
        """

        return Point2.new(x, y, parent=self)

    @property
    def right(self) -> Coordinate[XAxisT]:
        """
        Right.
        """

        return self.left + self.width

    @property
    def top(self) -> YAxisT:
        """
        Top.
        """

        return self.position.coordinates[1]

    @property
    def width(self) -> XLengthT:
        """
        Width.
        """

        return self.volume.lengths[0]
