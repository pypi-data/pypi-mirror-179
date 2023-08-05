from typing import Optional, Type, TypeVar

from bounden.protocols import VolumeProtocol
from bounden.volumes.percent import Percent
from bounden.volumes.volume import Volume


class Volume2(Volume):
    """
    A two-dimensional volume.
    """

    @classmethod
    def new(
        cls: Type["Volume2T"],
        width: float | int | Percent,
        height: float | int | Percent,
        parent: Optional[VolumeProtocol] = None,
    ) -> "Volume2T":
        """
        Creates a new `Volume2`.
        """

        return cls(width, height, parent=parent)

    @property
    def height(self) -> float | int:
        """
        Height.
        """

        return self.absolute(1)

    @property
    def width(self) -> float | int:
        """
        Width.
        """

        return self.absolute(0)


Volume2T = TypeVar("Volume2T", bound=Volume2)
