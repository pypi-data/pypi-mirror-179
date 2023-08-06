from typing import Callable, Generic, Optional

from bounden.coordinates.types import AxesT
from bounden.protocols import VectorProtocol
from bounden.vectors.types import LengthsT

AxisTranslator = Callable[[AxesT, LengthsT], AxesT]


class Vector(VectorProtocol, Generic[LengthsT]):
    """
    An n-dimensional vector.

    `lengths` describes the length of the vector in each dimension. The index
    indicates the dimension and the value describes the length. Pass `None` to
    describe a zero vector.
    """

    def __init__(self, lengths: Optional[LengthsT] = None) -> None:
        self._lengths = lengths

    def __bool__(self) -> bool:
        if self._lengths is None:
            return False

        for length in self._lengths:
            if length != 0:
                return True

        return False

    def __getitem__(self, index: int) -> float:
        if self._lengths is None:
            return 0
        return self._lengths[index]

    def __len__(self) -> int:
        return 0 if self._lengths is None else len(self._lengths)

    def __repr__(self) -> str:
        return str(self._lengths) if self._lengths else "<zero>"
