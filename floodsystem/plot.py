import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np


def plot_water_levels(station, dates, levels):
    """Plots water level data against time for a given station."""

    if not dates or not levels:
        print(f"No data available for {station.name}.")
        return

    # Plot water levels
    plt.plot(dates, levels, label="Water Level")

    # Plot typical low and high levels
    if station.typical_range:
        low, high = station.typical_range
        plt.axhline(y=low, color='r', linestyle='--', label="Typical Low")
        plt.axhline(y=high, color='g', linestyle='--', label="Typical High")

    # Labels and title
    plt.xlabel("Date")
    plt.ylabel("Water Level (m)")
    plt.xticks(rotation=45)
    plt.title(f"Water Levels for {station.name}")

    plt.legend()
    plt.tight_layout()  # Ensures proper formatting
    plt.show()
    
    plt.savefig('Task2E.png', dpi = 500)
    
def plot_water_level_with_fit(station, dates, levels, poly, d0):
    """Plots water level data and polynomial fit."""

    if not dates or not levels:
        print(f"No data available for {station.name}")
        return

    # Convert dates to numbers
    num_dates = [mdates.date2num(date) for date in dates]

    # Generate x values for the polynomial
    x_fit = np.linspace(min(num_dates), max(num_dates), 100)
    y_fit = poly(x_fit - d0)

    # Plot actual water levels
    plt.plot(dates, levels, 'o', label="Water Levels")

    # Plot polynomial fit
    plt.plot(mdates.num2date(x_fit), y_fit, 'r--', label="Polynomial Fit")

    # Plot typical range
    if station.typical_range:
        plt.axhline(y=station.typical_range[0], color='g', linestyle='--', label="Typical Low")
        plt.axhline(y=station.typical_range[1], color='r', linestyle='--', label="Typical High")

    # Labels and legend
    plt.xlabel("Date")
    plt.ylabel("Water Level (m)")
    plt.title(f"Water Level Fit for {station.name}")
    plt.xticks(rotation=45)
    plt.legend()
    plt.savefig('Task2F.png', dpi = 500)