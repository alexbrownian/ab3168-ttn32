import datetime
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.analysis import polyfit

def run():
    stations = build_station_list(use_cache=True)
    update_water_levels(stations)

    top_stations = stations_highest_rel_level(stations, 5)
    dt = datetime.timedelta(days=2)

    for station, _ in top_stations:
        dates, levels = fetch_measure_levels(station.measure_id, dt)
        
        if not dates or not levels:
            print(f"No data for {station.name}")
            continue
        
        poly, d0 = polyfit(dates, levels, 4)
        plot_water_level_with_fit(station, dates, levels, poly, d0)

if __name__ == "__main__":
    run()