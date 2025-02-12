import datetime
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_levels

def run():
    """Fetch and plot water levels for the top 5 stations with highest relative water levels."""

    # Build station list and update water levels
    stations = build_station_list(use_cache=True)
    update_water_levels(stations)

    # Get the top 5 stations with the highest relative levels
    top_stations = stations_highest_rel_level(stations, 5)

    dt = datetime.timedelta(days=10)

    for station, _ in top_stations:
        # Fetch water level data
        dates, levels = fetch_measure_levels(station.measure_id, dt)

        # Plot water levels
        plot_water_levels(station, dates, levels)

if __name__ == "__main__":
    run()