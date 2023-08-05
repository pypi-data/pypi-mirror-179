from typing import Any, Iterator, List, Optional, TypeVar

from bounden.log import log
from bounden.protocols import VolumeProtocol
from bounden.volumes.percent import Percent


class Volume(VolumeProtocol):
    """
    An n-dimensional volume.

    `lengths` describes the length of each dimension.
    """

    def __init__(
        self,
        *lengths: float | int | Percent,
        parent: Optional[VolumeProtocol] = None,
    ) -> None:
        self._lengths = lengths
        self._parent = parent

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Volume):
            return bool(list(self) == list(other))

        return bool(self._lengths == other)

    def __iter__(self) -> Iterator[float | int]:
        for dimension in range(len(self._lengths)):
            yield self.absolute(dimension)

    def __len__(self) -> int:
        return len(self._lengths)

    def __repr__(self) -> str:
        return str(self._lengths)

    def absolute(self, dimension: int) -> float | int:
        """
        Gets the absolute length of `dimension`.
        """

        length = self._lengths[dimension]

        if isinstance(length, (float, int)):
            return length

        if not self._parent:
            raise ValueError(
                f"{self.__class__.__name__} {repr(self)} cannot calculate "
                f"relative length {repr(length)} at dimension {dimension} "
                "without a parent volume"
            )

        return length.calculate(self._parent.absolute(dimension))

    def expand(self: "VolumeT", distance: float | int) -> "VolumeT":
        """
        Gets a copy of this volume expanded by `distance`.

        Pass a negative distance to contract.
        """

        ll: List[float | int | Percent] = []

        for length in self._lengths:
            if isinstance(length, (float, int)):
                ll.append(length + distance)
            else:
                log.warning("Will not expand relative length")
                ll.append(length)

        return self.__class__(*ll)


VolumeT = TypeVar("VolumeT", bound=Volume)
