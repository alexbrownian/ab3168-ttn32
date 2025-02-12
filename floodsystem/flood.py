from floodsystem.stationdata import update_water_levels, build_station_list

def stations_level_over_threshold(stations, tol):
    """Returns a sorted list of (station, relative level) tuples where the relative water level is above tol."""
    result = []

    for station in stations:
        relative_level = station.relative_water_level()
        if relative_level is not None and relative_level > tol:
            result.append((station, relative_level))

    # Sort stations by relative level in descending order
    return sorted(result, key=lambda x: x[1], reverse=True)

def print_stations_and_level(stations_list):
    """Prints station names with their latest water level."""
    for station, level in stations_list:
        print(f"{station.name}: {level:.2f}")

def stations_highest_rel_level(stations, N):
    """Prints the N stations with the highest relative water levels."""
    
    tol = 0.8  # Assigned by the question
    stations_over_threshold = stations_level_over_threshold(stations, tol)

    # Print top N stations
    top_stations = stations_over_threshold[:N]
    print_stations_and_level(top_stations)
    return top_stations

# Load station data and update water levels
stations = build_station_list(use_cache=True)
update_water_levels(stations)

# Run function to print the top 5 stations with highest relative water levels
stations_highest_rel_level(stations, 5)
