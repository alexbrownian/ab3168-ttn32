from floodsystem.stationdata import build_station_list


def stations_level_over_threshold(stations, tol):
    pass

stations = build_station_list(use_cache=True)

def stations_highest_rel_level(stations, N):
    tol = 0.8 # assigned by the question
    stations_over_threshold = stations_level_over_threshold(stations, tol)
    sorted_station_over_threshold = sorted(stations_over_threshold, reverse = True)
    
    output = []
    
    if len(sorted_station_over_threshold) <= N:
        
    for i in range(N):
        try: 
            output += sorted_station_over_threshold[i]
        except:
            pass
    
    pass
