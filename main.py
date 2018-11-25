#!/usr/bin/env python

import argparse
import csv
from collections import namedtuple

from search import LinearSearch

DEFAULT_CITIES_PATH = 'cities.csv'
DEFAULT_POINTS_PATH = 'points.csv'
DEFAULT_OUTPUT_PATH = 'output.csv'

City = namedtuple('City', ['name', 'top_x', 'top_y', 'bottom_x', 'bottom_y'])
Point = namedtuple('point', ['id', 'x', 'y'])


def convert(row, _type):
    """Converts single row data into the specified _typ.

    Args:
        row (list): single row data.
        _type (namedtuple): it can be either City or Point.

    Returns:
        obj: it can be City or Point.

    """
    title = row[0]
    rest = [int(v) for v in row[1:]]
    return _type(title, *rest)


def convert_csv(path, _type):
    """Loads and converts given csv file into a list of objects.

    Args:
        path (str): csv file path.
        _type (namedtuple): it can be either City or Point.

    Returns:
        list: converted objects.

    """
    with open(path, 'r') as f:
        reader = csv.reader(f)

        # skip first line
        next(reader)

        data = [convert(row, _type) for row in reader]
        return data


def write_output(path, points, cities):
    """Extracts info and Writes output in a csv file, 4 columns format.

    Args:
        path (str): csv file path.
        points (list): list of output points.
        cities (list): list of matching cities, may contain None entries.

    Returns:
        None

    """
    with open(path, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['ID', 'X', 'Y', 'City'])
        writer.writerows(
            zip(
                [p.id for p in points],
                [p.x for p in points],
                [p.y for p in points],
                [c.name if c else "None" for c in cities]
            )
        )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--cities', type=str, default=DEFAULT_CITIES_PATH, help='cities csv file path')
    parser.add_argument('--points', type=str, default=DEFAULT_POINTS_PATH, help='points csv file path')
    parser.add_argument('--output', type=str, default=DEFAULT_OUTPUT_PATH, help='output csv file path')

    args = parser.parse_args()

    cities_path = args.cities
    points_path = args.points
    output_path = args.output

    # Read csv files.
    cities = convert_csv(cities_path, City)
    points = convert_csv(points_path, Point)

    # Process points.
    search = LinearSearch(cities)
    matched_cities = [search.find(point) for point in points]

    # Write output.
    write_output(output_path, points, matched_cities)
    print('matching cities written to {}'.format(output_path))


if __name__ == '__main__':
    main()
