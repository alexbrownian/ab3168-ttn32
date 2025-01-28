# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa

import math

def haversine(lat1, lon1, lat2, lon2):
    """
    Calculate the great-circle distance between two points on the Earth using the Haversine formula.

    Args:
    lat1, lon1: Latitude and longitude of the first point (in degrees).
    lat2, lon2: Latitude and longitude of the second point (in degrees).

    Returns:
    float: Distance between the two points in kilometers.
    """
    # Convert latitude and longitude from degrees to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    # Radius of Earth in kilometers
    R = 6371.0

    # Differences in coordinates
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    # Haversine formula
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Distance in kilometers
    distance = R * c

    return distance

def distance_calculator(stations: list, p: tuple):
    """
    Calculate the Haversine distance of each station in the list, 
    and create a list of the station and its distance
    """
    x = [] # empty list that follows the convention in the sort_by_key function
    for station in stations:
        # Fetch the coordinate
        station_coord = station.coord 
        
        # Compute haversine distance
        haversine_distance = haversine(station_coord[0], station_coord[1], p[0], p[1]) 
        
        # Append the station object and distance into x
        x.append([station.name, station.town, haversine_distance]) 
        
    return x

def stations_by_distance(stations: list, p: tuple):
    """
    Signature function to return a sorted list of stations with regards to the Haversine 
    distance from coordinate p.
    """
    # Create a list of stations and their corresponding distances
    x = distance_calculator(stations, p)
    
    # Sort the distance
    output_x = sorted_by_key(x, 2, reverse = False)
    
    return output_x
    
    
        
        
        
    



