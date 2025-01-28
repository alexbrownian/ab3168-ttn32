from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius

def test_stations_within_radius():
    """
    Test the stations_within_radius function for Cambridge city centre with a 10 km radius.
    """
    # Cambridge city centre coordinates
    cambridge_city_centre = (52.2053, 0.1218)
    radius = 10

    # Get all stations
    stations = build_station_list(use_cache=True)
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

    # Define the expected station names (update this to match the actual data)
    expected_station_names = [
        'Bin Brook', 'Cambridge Baits Bite', "Cambridge Byron's Pool",
        'Cambridge Jesus Lock', 'Comberton', 'Dernford', 'Girton',
        'Haslingfield Burnt Mill', 'Lode', 'Oakington', 'Stapleford'
    ]

    # Assert that the output matches the expected result
    assert station_names == expected_station_names
