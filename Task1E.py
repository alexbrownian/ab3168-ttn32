from floodsystem.geo import rivers_by_station_numbers
from floodsystem.stationdata import build_station_list

def run():
    """
    Requirements for Task 1E
    """
    
    # List of station names 
    stations_list = build_station_list(use_cache= True)
    
    # Use the number provided in the question, and output the list of 
    N = 9
    output_list = rivers_by_station_numbers(stations_list, N)
    
    print(output_list)
    
    return output_list
    
    



if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()