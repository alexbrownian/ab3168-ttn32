from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius

from .utils import sorted_by_key  # noqa

def stations_by_distance(stations: list, p: tuple):
    """
    Return a sorted list of stations with regards to the Haversine 
    distance from the given coordinate p.

    Args:
        stations (list): List of station objects.
        p (tuple): Latitude and longitude of the reference point.

    Returns:
        list: A list of tuples, where each tuple contains a station object
              and its distance from the point `p`, sorted by distance in ascending order.
    """
    x = distance_calculator(stations, p)
    x_sorted = sorted_by_key(x, 1)  # Sorting by the second element (distance)

    return x_sorted

