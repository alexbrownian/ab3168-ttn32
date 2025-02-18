from floodsystem.flood_warnings import assess_flood_risk
from floodsystem.stationdata import build_station_list, update_water_levels

def run():
    """Run flood risk assessment using a momentum quant approach."""
    
    # Fetch station data and update water levels
    stations = build_station_list(use_cache=True)
    update_water_levels(stations)

    # Assess flood risk
    risk_df = assess_flood_risk(stations)

    # Print results
    print("Top 10 Towns with Highest Flood Risk:")
    print(risk_df.head(10))

    # Save to CSV
    #risk_df.to_csv("flood_risk.csv", index=False)

if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()