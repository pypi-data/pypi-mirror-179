from bounden.coordinates.coordinate import Coordinate


class IntegerCoordinate(Coordinate[int]):
    """
    A coordinate on an integer axis.
    """

    def __float__(self) -> float:
        return float(self.coordinate)

    def translate(self, distance: float) -> "IntegerCoordinate":
        """
        Gets a copy of this coordinate translated by the integer value of
        `distance`.
        """

        return IntegerCoordinate(self.coordinate + int(distance))
