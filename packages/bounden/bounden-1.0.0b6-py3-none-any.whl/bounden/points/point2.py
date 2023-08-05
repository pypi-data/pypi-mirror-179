from typing import Optional

from bounden.coordinates.types import XAxisT, YAxisT
from bounden.points.point import Point
from bounden.protocols import RegionProtocol


class Point2(Point[tuple[XAxisT, YAxisT]]):
    """
    A point in two-dimensional space.

    `x` and `y` are the x and y coordinates respectively.
    """

    def __init__(
        self,
        x: XAxisT,
        y: YAxisT,
        parent: Optional[RegionProtocol] = None,
    ) -> None:
        super().__init__((x, y), parent=parent)

    @property
    def x(self) -> XAxisT:
        """
        X coordinate.
        """

        return self.coordinates[0]

    @property
    def y(self) -> YAxisT:
        """
        Y coordinate.
        """

        return self.coordinates[1]
