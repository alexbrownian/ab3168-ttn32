from floodsystem.stationdata import build_station_list


def stations_level_over_threshold(stations, tol):
    pass

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
