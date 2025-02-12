def stations_level_over_threshold(stations, tol):
    output = []
    for station in stations:
        level = station.relative_water_level()
        if level is not None and level > tol:
            output.append((station, level))
    output.sort(key=lambda x: x[1], reverse=True)
    
    return output

def stations_highest_rel_level(stations, N):
    valid_stations = []
    for station in stations:
        level = station.relative_water_level()
        if level is not None:
            valid_stations.append((station, level))
    
    valid_stations.sort(key=lambda x: x[1], reverse=True)
    return valid_stations[:N]