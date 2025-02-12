import pandas as pd
import numpy as np
import datetime
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels

# Define moving average periods
FAST_MA_DAYS = 2  # Short-term MA (last 2 days)
SLOW_MA_DAYS = 10  # Long-term MA (last 10 days)

def moving_average(data, window_size):
    """Compute simple moving average over a given window size."""
    if len(data) < window_size:
        return None  # Not enough data for moving average
    return np.mean(data[-window_size:])  # Compute average of last window_size values

def assess_flood_risk(stations):
    """Assess flood risk based on moving averages of water levels."""
    
    risk_data = []

    for station in stations:
        # Fetch last 10 days of water level data
        dt = datetime.timedelta(days=SLOW_MA_DAYS)
        dates, levels = fetch_measure_levels(station.measure_id, dt)

        if not dates or not levels or len(levels) < SLOW_MA_DAYS:
            continue  # Skip stations with insufficient data

        # Compute moving averages
        fast_ma = moving_average(levels, FAST_MA_DAYS)
        slow_ma = moving_average(levels, SLOW_MA_DAYS)

        if fast_ma is None or slow_ma is None or slow_ma == 0:
            continue  # Skip if moving averages cannot be computed

        # Compute risk level based on ratio
        ratio = fast_ma / slow_ma
        if ratio > 1.5:
            risk_level = "Severe"
        elif ratio > 1.2:
            risk_level = "High"
        elif ratio > 0.8:
            risk_level = "Moderate"
        else:
            risk_level = "Low"

        risk_data.append({"Station": station.name, "Town": station.town, "Fast MA": fast_ma, "Slow MA": slow_ma, "Ratio": ratio, "Risk": risk_level})

    # Convert to DataFrame and sort by risk
    risk_df = pd.DataFrame(risk_data)
    risk_df = risk_df.sort_values(by="Ratio", ascending=False)

    return risk_df

def run():
    """Run flood risk assessment using moving averages."""
    
    # Fetch station data and update water levels
    stations = build_station_list(use_cache=True)
    update_water_levels(stations)

    # Assess flood risk
    risk_df = assess_flood_risk(stations)

    # Print top 10 most at-risk stations
    print("\nTop 10 Stations Most at Risk of Flooding:")
    print(risk_df.head(10)[["Station", "Town", "Risk", "Ratio"]])

if __name__ == "__main__":
    run()