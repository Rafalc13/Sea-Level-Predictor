import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig = plt.subplots()
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    data = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x = pd.Series(range(1880, 2051))
    y = data.slope * x + data.intercept
    plt.plot(x, y, color='red')
    # print(data.slope, data.pvalue, data.intercept, x, y)

    # Create second line of best fit
    new_df = df[df['Year'] >= 2000]
    new_data = linregress(new_df['Year'], new_df['CSIRO Adjusted Sea Level'])
    new_x = pd.Series(range(2000, 2051))
    new_y = new_data.slope * new_x + new_data.intercept
    plt.plot(new_x, new_y, color='green')
    # print(new_data, new_x, new_y)


    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()