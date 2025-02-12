import matplotlib.pyplot as plt

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