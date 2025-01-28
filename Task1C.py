from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius

def run():
    """
    Build a list of stations within 10 km of Cambridge city centre
    and print their names in alphabetical order.
    """
    # IDeeal radius and coordinates
    cambridge_city_centre = (52.2053, 0.1218)
    radius = 10

    stations = build_station_list(use_cache=True) # change to false for the FR code
    stations_in_radius = stations_within_radius(stations, cambridge_city_centre, radius)

    # Get station names and sort them
    station_names = []
    for station in stations_in_radius:
        station_names.append(station.name)
    station_names.sort()

    # Print stations
    print("Stations near Cambridge:")
    for name in station_names:
        print(name)

if __name__ == "__main__":
    print("Task 1C: Find stations near Cambridge")
    run()
