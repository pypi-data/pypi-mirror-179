from bounden.coordinates.coordinate import Coordinate


class FloatCoordinate(Coordinate[float]):
    """
    A coordinate on a floating point axis.
    """

    def __float__(self) -> float:
        return self.coordinate

    def translate(self, distance: float) -> "FloatCoordinate":
        """
        Gets a copy of this coordinate translated by `distance`.
        """

        return FloatCoordinate(self.coordinate + distance)
