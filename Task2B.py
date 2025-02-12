from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold

def run():
    """Task 2B: Identify and print stations over threshold"""

    # Build list of stations
    stations = build_station_list(use_cache = True)
    
    # Update stations with latest water level data
    update_water_levels(stations)

    # Define threshold for risk assessment
    threshold = 0.8

    # Get stations with relative water levels over threshold
    risky_stations = stations_level_over_threshold(stations, threshold)

    # Print stations in the format: "Station name: relative level"
    for station, level in risky_stations:
        print(f"{station.name}: {level:.2f}")

if __name__ == "__main__":
    run()
