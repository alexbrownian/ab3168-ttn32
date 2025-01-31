# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa

import math

# Task 1B

def haversine_helper(lat1, lon1, lat2, lon2):
    """
    Calculate the great-circle distance between two points on the Earth using the Haversine module.

    Args:
    lat1, lon1: Latitude and longitude of the first point (in degrees).
    lat2, lon2: Latitude and longitude of the second point (in degrees).

    Returns:
    float: Distance between the two points in kilometers.
    """
    from haversine import haversine, Unit
    # Convert latitude and longitude from degrees to radians
    position1 = (lat1, lon1)
    position2 = (lat2, lon2)

    # Haversine formula
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Distance in kilometers
    distance = R * c

    return distance

def distance_calculator(stations: list, p: tuple):
    x = [] # empty list that follows the convention in the sort_by_key function
    for station in stations:
        station_coord = station.coord 
        
        # Compute haversine distance
        haversine_distance = haversine(station_coord[0], station_coord[1], p[0], p[1]) 
        
        # Appending the station object and distance into x
        x.append([station.name, station.town, haversine_distance]) 
        
    return x

def stations_by_distance(stations: list, p: tuple):
    # Create a list of stations and their corresponding distances
    x = distance_calculator(stations, p)
    
    # Sort the distance
    output_x = sorted_by_key(x, 2, reverse = False)
    
    return output_x

#Task 1C - 1D 
#TASK 1C
def stations_within_radius(stations, centre, r):
    result = []
    for station in stations:
        distance = haversine_helper(station.coord[0], station.coord[1], centre[0], centre[1])

        # Check if the station is within the radius
        if distance <= r:
            result.append(station)
    return result

#TASK 1D
#Empty Set
def rivers_with_station(stations):
    rivers = set() # to prevent duplicates

    for station in stations:
        print(station.river)
        if station.river and station.river.strip():  # Checking if the station has a river attribute
            rivers.add(station.river)

    return rivers
#to be fixed (1052) but lets seeeeee?

#making a dicitonary:
def stations_by_river(stations):
    river_dict = {} 
     
    for station in stations:
        if station.river and station.river.strip():  # Ensure river name is valid
            if station.river not in river_dict:
                river_dict[station.river] = []  
            river_dict[station.river].append(station)  # Add station to the river's list

    return river_dict
                
# TASK 1E
## Essentially, Task 1E is built on Task 1D. Task 1D outputs the stations along a river. 
def rivers_by_station_numbers(stations, N):
    # generate dictionary from 1D
    station_dict = stations_by_river(stations) 
    
    # Counting
    river_count = [] # list of tuples. Each tuple contains the river name (str) and number of stations (int)
    for river, stations in station_dict.items():
        river_count.append((river, len(stations))) # Create a tuple of the required data, and add it into the river_count
    
    sorted_river_count = sorted_by_key(river_count, 1, reverse= True) # Sort according to the number of stations,
    # in descending order
        
    capped_sorted_river_count = sorted_river_count[:N]
    
    return capped_sorted_river_count # return the river count by the cap
    
        
    
    
    
    
    



