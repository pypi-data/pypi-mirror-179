from bounden.volumes.types import XLengthT, YLengthT
from bounden.volumes.volume import Volume


class Volume2(Volume[tuple[XLengthT, YLengthT]]):
    """
    A two-dimensional volume.

    `width` and `height` describe the volume's width and height.
    """

    @classmethod
    def new(
        cls,
        width: XLengthT,
        height: YLengthT,
    ) -> "Volume2[XLengthT, YLengthT]":
        """
        Creates a new `Volume2`.
        """

        return Volume2((width, height))

    @property
    def height(self) -> YLengthT:
        """
        Height.
        """

        return self.lengths[1]

    @property
    def width(self) -> XLengthT:
        """
        Width.
        """

        return self.lengths[0]
