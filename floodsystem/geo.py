# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa

def stations_within_radius(stations, centre, r):
    result = []
    for station in stations:
        dx = station.coord[0] - centre[0]
        dy = station.coord[1] - centre[1]
        distance = (dx**2 + dy**2)**0.5*111

        if distance <= r:
            result.append(station)
    return result
