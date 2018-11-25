def within(point, city):
    """Checks whether a point is within city.

    Args:
        point (obj): Point object to be checked against city borders.
        city  (obj): City object describes coordinates of the city.

    Returns:
        bool: True if the point is withing the city, otherwise False.

    """
    return city.top_x <= point.x <= city.bottom_x and city.top_y <= point.y <= city.bottom_y


class BaseSearch:
    """BaseSearch provides method to find a city that wraps the point"""

    def __init__(self, cities):
        self.cities = cities

    def find(self, point):
        raise NotImplementedError


class LinearSearch(BaseSearch):
    """LinearSearch is an implementation of BaseSearch based on linear search algorithm"""

    def __init__(self, cities):
        super().__init__(cities)

    def find(self, point):
        """Finds which city contains the given point.

        Args:
            point (obj): coordinates of the point.

        Returns:
            obj: city which contains the point or None.

        """
        for city in self.cities:
            if within(point, city):
                return city
