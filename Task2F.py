
import pandas as pd
import numpy as np
import datetime
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels

# Define moving average periods (in days)
FAST_MA_DAYS = 2   # Short-term moving average (last 2 days)
SLOW_MA_DAYS = 10  # Long-term moving average (last 10 days)


def moving_average(data, window_size):
    """Compute the simple moving average over the last window_size data points."""
    if len(data) < window_size:
        return None  # Not enough data to compute the moving average
    return np.mean(data[-window_size:])


def assess_flood_risk(stations):
    """Assess flood risk at each station based on moving averages of water levels."""
    risk_data = []

    for station in stations:
        # Retrieve water level readings for the past 10 days
        dt = datetime.timedelta(days=SLOW_MA_DAYS)
        dates, levels = fetch_measure_levels(station.measure_id, dt)

        if not dates or not levels or len(levels) < SLOW_MA_DAYS:
            continue  # Skip if insufficient data

        # Compute moving averages
        fast_ma = moving_average(levels, FAST_MA_DAYS)
        slow_ma = moving_average(levels, SLOW_MA_DAYS)

        if fast_ma is None or slow_ma is None or slow_ma == 0:
            continue  # Skip if unable to compute averages

        # Compute ratio of fast to slow moving average
        ratio = fast_ma / slow_ma

        # Determine risk level based on ratio
        if ratio > 1.5:
            risk_level = "Severe"
        elif ratio > 1.2:
            risk_level = "High"
        elif ratio > 0.8:
            risk_level = "Moderate"
        else:
            risk_level = "Low"

        risk_data.append({
            "Station": station.name,
            "Town": station.town,
            "Fast MA": fast_ma,
            "Slow MA": slow_ma,
            "Ratio": ratio,
            "Risk": risk_level
        })

    # Create a DataFrame for easy sorting and display
    risk_df = pd.DataFrame(risk_data)
    risk_df = risk_df.sort_values(by="Ratio", ascending=False)
    return risk_df


def run():
    """Run the flood risk assessment and print the top 10 stations most at risk."""
    # Build the station list and update their latest water levels
    stations = build_station_list(use_cache=True)
    update_water_levels(stations)

    # Assess flood risk based on the moving averages of water levels
    risk_df = assess_flood_risk(stations)

    # Display the top 10 stations with the highest risk ratios
    print("\nTop 10 Stations Most at Risk of Flooding:")
    print(risk_df.head(10)[["Station", "Town", "Risk", "Ratio"]])


if __name__ == "__main__":
    run()