from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station, stations_by_river

def Task1D():
    stations = build_station_list()

    # Part 1: Rivers with at least one monitoring station
    rivers = rivers_with_station(stations)
    print(f"{len(rivers)} stations. First 10 - {sorted(list(rivers))[:10]}")

    river_dict = stations_by_river(stations)
    # Print stations on 'River Aire', 'River Cam', and 'River Thames'
    for river in ['River Aire', 'River Cam', 'River Thames']:
        if river in river_dict:
            station_names = sorted([station.name for station in river_dict[river]])
            print(f"Stations on {river}: {station_names}")
        else: #Basically not in the dictionary (or entry val)
            print(f"No stations found on {river}.")

if __name__ == "__main__":
    print("Task 1D")
    Task1D()
