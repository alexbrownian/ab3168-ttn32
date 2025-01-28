from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations

def run():
    """
    Requirement for 1F. End of Milestone 1 LETSGOOO"""
    
    # List of station names 
    stations_list = build_station_list(use_cache= True)
    
    output = inconsistent_typical_range_stations(stations_list)
    
    print(output)
    return output

if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()


    