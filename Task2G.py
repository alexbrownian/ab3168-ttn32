import datetime
import matplotlib.dates as mdates
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.analysis import polyfit

def run():
    """Assess flood risk for towns based on water level trends."""
    stations = build_station_list(use_cache=True)
    update_water_levels(stations)

    # Get top 10 stations with the highest relative water levels
    top_stations = stations_highest_rel_level(stations, 10)
    dt = datetime.timedelta(days=2)  # Analyze past 2 days of data

    town_risk = {}

    for station, rel_level in top_stations:
        if station.town is None:
            continue  # Skip stations without town data

        dates, levels = fetch_measure_levels(station.measure_id, dt)

        if not dates or not levels:
            print(f"No data for {station.name}")
            continue
        
        # Fit a 4th-degree polynomial to the data
        poly, d0 = polyfit(dates, levels, 4)

        # Convert the most recent datetime to a float for polynomial evaluation.
        most_recent_time = mdates.date2num(dates[-1])
        
        # Estimate the trend by evaluating the derivative of the polynomial at the most recent time (offset by d0)
        recent_derivative = poly.deriv()(most_recent_time - d0)

        # Determine risk based on relative water level and trend.
        # Criteria based on relative water level:
        # > 2.0: Severe, 1.5-2.0: High, 1.0-1.5: Moderate, < 1.0: Low
        if rel_level > 2.0:
            risk = "Severe"
        elif rel_level > 1.5:
            risk = "High"
        elif rel_level > 1.0:
            risk = "Moderate"
        else:
            risk = "Low"

        # Adjust risk based on the trend: a rapidly rising water level increases risk; a falling level lowers risk.
        if recent_derivative > 0.1:
            if risk == "High":
                risk = "Severe"
            elif risk == "Moderate":
                risk = "High"
            elif risk == "Low":
                risk = "Moderate"
        elif recent_derivative < -0.1:
            if risk == "Severe":
                risk = "High"
            elif risk == "High":
                risk = "Moderate"
            elif risk == "Moderate":
                risk = "Low"

        # Store risk level for the town
        town_risk[station.town] = risk

    # Print flood risk assessment by town
    for town, risk in town_risk.items():
        print(f"{town}: {risk} risk")

if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()