from stationdata import update_water_levels, build_station_list


def stations_level_over_threshold(stations, tol):
    result = []

    for station in stations:
        relative_level = station.relative_water_level()

        # Consider only valid stations with relative level above threshold
        if relative_level is not None and relative_level > tol:
            result.append((station, relative_level))

    # Sort stations by relative level in descending order
    result.sort(key=lambda x: x[1], reverse=True)

    return result

stations = build_station_list(use_cache=True)

def print_stations_and_level(stations_list):
    # Given the list of Station Objects, print the list of stations
    for station in stations_list:
        print(str(station.name) + ' ' + str(station.latest_level))

def stations_highest_rel_level(stations, N):
    # Print N stations with highest relative water level. 
    
    tol = 0.8 # assigned by the question
    stations_over_threshold = stations_level_over_threshold(stations, tol)
    sorted_station_over_threshold = sorted(stations_over_threshold, reverse = True)
    
    if len(sorted_station_over_threshold) <= N:
        print_stations_and_level(sorted_station_over_threshold)
    else:
        print_stations_and_level(sorted_station_over_threshold[:N])
        return sorted_station_over_threshold[:N]