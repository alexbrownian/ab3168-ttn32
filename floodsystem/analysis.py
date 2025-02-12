import numpy as np
import matplotlib.dates as mdates

def polyfit(dates, levels, p):
    """Fits a polynomial of degree p to water level data."""

    if not dates or not levels:
        return None, None

    # Convert dates to numerical format
    num_dates = []
    for date in dates:
        num_dates.append(mdates.date2num(date))

    # Shift time axis to start at 0
    d0 = num_dates[0]
    shifted_dates = []
    for d in num_dates:
        shifted_dates.append(d - d0)

    # Fit polynomial
    poly_coeff = np.polyfit(shifted_dates, levels, p)

    # Create polynomial function
    poly = np.poly1d(poly_coeff)
    
    return poly, d0