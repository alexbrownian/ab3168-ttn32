from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level

def run():
    stations = build_station_list(use_cache=True)
    update_water_levels(stations)
    
    top_stations = stations_highest_rel_level(stations, 10)

    for station, level in top_stations:
        print(station.name, level)

if __name__ == "__main__":
    run()