from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list

def run():
    """
    Requirements for Task 1B
    """
    
    # List of station names 
    stations_list = build_station_list(use_cache= True)

    # Sort the stations as required
    Cambridge_coordinate = (52.2053, 0.1218)
    sorted_stations_by_distance = stations_by_distance(stations_list, Cambridge_coordinate)

    # Define x to match the requirement in question (for testing)
    x = sorted_stations_by_distance

    print(sorted_stations_by_distance)

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()