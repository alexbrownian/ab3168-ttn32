from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius

def run():
    """
    Build a list of stations within 10 km of Cambridge city centre
    and print their names in alphabetical order.
    """
    # Define the Cambridge city centre coordinates
    cambridge_city_centre = (52.2053, 0.1218)

    # Define the radius (10 km)
    radius = 10

    # Build the list of stations
    stations = build_station_list(use_cache=True)

    # Get stations within the radius
    stations_in_radius = stations_within_radius(stations, cambridge_city_centre, radius)

    # Extract and sort station names alphabetically
    station_names = sorted([station.name for station in stations_in_radius])

    # Print the sorted station names
    print(station_names)

if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()
