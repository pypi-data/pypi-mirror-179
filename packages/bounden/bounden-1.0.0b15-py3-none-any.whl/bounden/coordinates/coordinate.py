from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

ValueT = TypeVar("ValueT")


class Coordinate(ABC, Generic[ValueT]):
    """
    Abstract base coordinate.
    """

    def __init__(self, coordinate: ValueT) -> None:
        self.coordinate = coordinate

    def __add__(self: "CoordinateT", other: Any) -> "CoordinateT":
        return self.translate(self.parse(other))

    @abstractmethod
    def __float__(self) -> float:
        """
        Override to return the float value of this coordinate.
        """

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Coordinate):
            o: Coordinate[Any] = other
            return bool(self.coordinate == o.coordinate)

        return bool(self.coordinate == other)

    def __repr__(self) -> str:
        return str(self.coordinate)

    def __sub__(self: "CoordinateT", other: Any) -> "CoordinateT":
        return self.translate(-self.parse(other))

    @classmethod
    def parse(cls, other: Any) -> float | int:
        """
        Attempts to parse `other` to an float or integer.
        """

        if isinstance(other, (float, int)):
            return other

        raise ValueError(
            f"{cls.__name__} could not parse {repr(other)} "
            f"({other.__class__.__name__}) as a float or int"
        )

    @abstractmethod
    def translate(self: "CoordinateT", distance: float) -> "CoordinateT":
        """
        Gets a copy of this coordinate translated by `distance`.
        """


CoordinateT = TypeVar("CoordinateT", bound=Coordinate[Any])
