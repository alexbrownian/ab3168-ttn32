from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius

def run():
    stations = build_station_list()

    cambridge_center = (52.2053, 0.1218)
    nearby_stations = stations_within_radius(stations, cambridge_center, 10) 
    # pull from the Geo.py doc

    print(sorted([station.name for station in nearby_stations]))

if __name__ == "__main__":
    run()
