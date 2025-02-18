from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem import flood

def run():
    stations = build_station_list(use_cache=True)
    update_water_levels(stations)
    tol = 0.8
    over_threshold = flood.stations_level_over_threshold(stations, tol)
    
    for station, level in over_threshold:
        print(station.name, level)

if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()