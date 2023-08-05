from typing import Any, Type, TypeVar

from bounden.volumes.types import XLengthT, YLengthT
from bounden.volumes.volume import Volume


class Volume2(Volume[tuple[XLengthT, YLengthT]]):
    """
    A two-dimensional volume.
    """

    @classmethod
    def new(
        cls: Type["Volume2T"],
        width: XLengthT,
        height: YLengthT,
    ) -> "Volume2T":
        """
        Creates a new `Volume2`.
        """

        return cls((width, height))

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


Volume2T = TypeVar("Volume2T", bound=Volume2[Any, Any])
