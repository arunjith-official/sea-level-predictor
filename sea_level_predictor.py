import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df=pd.read_csv('./epa-sea-level.csv')
    years = df["Year"]
    sea_levels = df["CSIRO Adjusted Sea Level"]
    # Create scatter plot
    plt.scatter(years,sea_levels)
    plt.title("Change in sealevel according to the years")
    plt.xlabel('Year')
    plt.ylabel('CSIRO Adjusted Sea level')
    plt.show


    # Create first line of best fit
    result1 = linregress(years, sea_levels)
    future_years = np.arange(min(years),2051)
    predicted_sea_levels = result1.slope * future_years + result1.intercept
    plt.plot(future_years,predicted_sea_levels,label = "Line of Best Fit", color="Red" )
    
    # Create second line of best fit
    recent_years = df[df['Year']>=2000]
    result2 = linregress(recent_years["Year"], recent_years["CSIRO Adjusted Sea Level"])
    recent_future_years = np.arange(2000,2051)
    recent_predicted_sea_levels = result2.slope * recent_future_years + result2.intercept
    plt.plot(recent_future_years, recent_predicted_sea_levels, label= "Line of Best Fit", color="red")
    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()