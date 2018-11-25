import unittest
from collections import namedtuple

from search import LinearSearch

City = namedtuple('City', ['name', 'top_x', 'top_y', 'bottom_x', 'bottom_y'])
Point = namedtuple('point', ['id', 'x', 'y'])


class TestSearch(unittest.TestCase):
    def setUp(self):
        self.search_algorithms = [(LinearSearch, 'linear search')]

    def get_cities(self, lst):
        return [
            City(str(i), *row) for i, row in enumerate(lst)
        ]

    def get_points(self, lst):
        return [
            Point(str(i), *row) for i, row in enumerate(lst)
        ]

    def check(self, cities, points, expected):
        for a, a_name in self.search_algorithms:
            s = a(cities)
            for point, city in zip(points, expected):
                output = s.find(point)
                self.assertEqual(city, output, msg='Used algorithm "{}"'.format(a_name))

    def test_visualization_example(self):
        cities = self.get_cities([(2, 2, 5, 4), (6, 6, 10, 7)])
        points = self.get_points([(2, 2), (5, 4), (6, 6), (10, 7), (9, 2), (3, 3), (6, 7)])
        expected = [cities[0], cities[0], cities[1], cities[1], None, cities[0], cities[1]]

        self.check(cities, points, expected)

    def test_input_sample(self):
        cities = self.get_cities([(1, 1, 5, 6), (10, 1, 13, 2)])
        points = self.get_points([(2, 1), (10, 1), (100, 1000)])
        expected = [cities[0], cities[1], None]

        self.check(cities, points, expected)

    def test_complex_example(self):
        cities = self.get_cities([(2, 2, 6, 4), (4, 6, 8, 12), (14, 4, 26, 12), (2, 14, 22, 20)])
        # Q R T S B1 A1 C1 U Z
        points = self.get_points([(4, 3), (6, 8), (24, 6), (18, 10), (4, 16), (14, 18), (20, 16), (10, 12), (24, 18)])
        expected = [cities[0], cities[1], cities[2], cities[2], cities[3], cities[3], cities[3], None, None]

        self.check(cities, points, expected)


if __name__ == '__main__':
    unittest.main()
