from floodsystem.stationdata import build_station_list

def name_of_each_station(self):
    stations = build_station_list(use_cache=True)
    overflowing_stations = []
    for i in stations:
        if stations.relative_water_level() > 0.8:
            overflowing_stations.append(i)
    return overflowing_stations

name_of_each_station(self)