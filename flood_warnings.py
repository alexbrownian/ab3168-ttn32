import pandas as pd
import numpy as np
import datetime
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels

# Define moving average periods
short_window = 2  # Fast MA (e.g., last 2 days)
long_window = 10  # Slow MA (e.g., last 10 days)

def moving_averages(water_levels, dates):
    """Calculate short-term and long-term moving averages for water levels."""
    
    if len(water_levels) < long_window:
        return None, None  # Not enough data to calculate MAs
    
    # Convert dates to numeric format
    levels_series = pd.Series(water_levels, index=pd.to_datetime(dates))
    
    # Calculate moving averages
    fast_ma = levels_series.rolling(window=short_window).mean().iloc[-1]  # Short-term MA
    slow_ma = levels_series.rolling(window=long_window).mean().iloc[-1]  # Long-term MA
    
    return fast_ma, slow_ma

def assess_flood_risk(stations):
    """Assess flood risk based on moving averages."""
    
    risk_data = []

    for station in stations:
        # Fetch last 10 days of water level data
        dt = datetime.timedelta(days=10)
        dates, levels = fetch_measure_levels(station.measure_id, dt)

        if not dates or not levels:
            continue  # Skip stations with no data

        # Compute moving averages
        fast_ma, slow_ma = moving_averages(levels, dates)

        if fast_ma is None or slow_ma is None or slow_ma == 0:
            continue  # Skip if moving averages cannot be computed

        # Compute ratio
        ratio = fast_ma / slow_ma

        # Classify risk level
        if ratio > 1.5:
            risk_level = "Severe"
        elif ratio > 1.2:
            risk_level = "High"
        elif ratio > 0.8:
            risk_level = "Moderate"
        else:
            risk_level = "Low"

        risk_data.append({"Town": station.town, "Fast MA": fast_ma, "Slow MA": slow_ma, "Ratio": ratio, "Risk": risk_level})

    # Convert to DataFrame and sort by risk
    risk_df = pd.DataFrame(risk_data)
    risk_df = risk_df.sort_values(by="Ratio", ascending=False)

    return risk_df