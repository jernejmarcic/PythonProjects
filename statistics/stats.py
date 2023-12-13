import math
import time
import csv
import numpy as np
import matplotlib.pyplot as plt
import statistics
import datetime
from mpl_toolkits.mplot3d import axes3d
import pandas as pd
import imageio
import os

today = datetime.date.today()
now = datetime.datetime.now()
filename = "GlobalTemperatures.csv"


def tempandtime():
    open_file = open(filename)
    file_parse = csv.DictReader(open_file)
    counter = 0
    temperatures = []
    dates = []
    for line in file_parse:
        print(line)
        if line["LandAverageTemperature"] == '':
            continue
        dt = datetime.datetime.strptime(line["dt"],"%Y-%m-%d")
        temp = float(line["LandAverageTemperature"])
        temperatures.append(temp)
        dates.append(dt)


    n = 200 # How many values do you want to mean
    middletemperatures = []
    middledates = dates[0:-n]
    for i in range(len(temperatures)-n):
        tempseveger = []
        for j in range(n):
            tempseveger.append(temperatures[i+j])
        meanT = statistics.mean(tempseveger)
        middletemperatures.append(meanT)


    plt.title("Global temperatures in the past 300 years")
    plt.xlabel("years")
    plt.yticks(np.arange(-5,20))
    plt.grid()
    plt.ylabel("°C")
    plt.plot(dates, temperatures)
    plt.plot(middledates,middletemperatures)


def convert_to_float(coord_str):
    """Convert coordinates with letters to float."""
    if 'N' in coord_str or 'E' in coord_str:
        return float(coord_str[:-1])
    if 'S' in coord_str or 'W' in coord_str:
        return -float(coord_str[:-1])
    return float(coord_str)

def scatterplot():
    """
    This function reads the temperature data, filters it for the year 2013, averages the 
    temperature by location, and then plots the averaged temperature data on a 3D scatter plot.
    """
    data = pd.read_csv('GlobalLandTemperaturesByCity.csv')

    """ Filter the data by year and create a copy """
    filtered_data = data[data['dt'].str.startswith('2013')].copy()

    """ Convert latitude and longitude to floats """
    filtered_data['Longitude'] = filtered_data['Longitude'].apply(convert_to_float)
    filtered_data['Latitude'] = filtered_data['Latitude'].apply(convert_to_float)

    """ Average out temperature data for each location """
    averaged_data = filtered_data.groupby(['Latitude', 'Longitude'])['AverageTemperature'].mean().reset_index()

    longitude = averaged_data['Longitude'].values
    latitude = averaged_data['Latitude'].values
    temperature = averaged_data['AverageTemperature'].values

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    """ Use scatter plot """
    ax.scatter(longitude, latitude, temperature, c=temperature, cmap='viridis')

    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')
    ax.set_zlabel('AverageTemperature')


def wireframe():
    """
    This function reads the temperature data, filters it for the year 2013, averages the 
    temperature by location, and then plots the averaged temperature data on a 3D wireframe plot.
    """
    data = pd.read_csv('GlobalLandTemperaturesByCity.csv')

    """ Filter the data by year and create a copy """
    filtered_data = data[data['dt'].str.startswith('2013')].copy()

    """ Convert latitude and longitude to floats """
    filtered_data['Longitude'] = filtered_data['Longitude'].apply(convert_to_float)
    filtered_data['Latitude'] = filtered_data['Latitude'].apply(convert_to_float)

    """ Average out temperature data for each location """
    averaged_data = filtered_data.groupby(['Latitude', 'Longitude'])['AverageTemperature'].mean().reset_index()

    """ Create a grid for the wireframe """
    x = np.linspace(averaged_data['Longitude'].min(), averaged_data['Longitude'].max(), len(averaged_data['Longitude'].unique()))
    y = np.linspace(averaged_data['Latitude'].min(), averaged_data['Latitude'].max(), len(averaged_data['Latitude'].unique()))
    X, Y = np.meshgrid(x, y)
    Z = pd.pivot_table(averaged_data, values='AverageTemperature', index='Latitude', columns='Longitude').values

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    """ Plot the wireframe """
    ax.plot_wireframe(X, Y, Z)

def scatter_plot_for_year_month(year_month, data):
    """Generate scatter plot for a specific year and month."""
    monthly_data = data[data['dt'] == year_month]

    longitude = monthly_data['Longitude'].values
    latitude = monthly_data['Latitude'].values
    temperature = monthly_data['AverageTemperature'].values

    fig, ax = plt.subplots()
    
    sc = ax.scatter(longitude, latitude, c=temperature, cmap='viridis', s=15)
    plt.colorbar(sc, ax=ax, label="AverageTemperature")
    
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')
    ax.set_title(f'Average Temperature for {year_month}')

    """ Save the scatter plot as an image """
    filename = f'scatter_{year_month}.png'
    plt.savefig(filename)
    plt.close()
    
    return filename

def create_gif(data, start_year, end_year, gif_filename='scatter_animation.gif'):
    """Generate GIF from scatter plots over the specified year range."""
    filenames = []

    unique_dates = sorted(data['dt'].unique())  
    for date in unique_dates:
        year = int(date.split('-')[0])
        if start_year <= year <= end_year:
            filename = scatter_plot_for_year_month(date, data)
            filenames.append(filename)

    """ Create a GIF from the images """
    images = [imageio.imread(filename) for filename in filenames]
    imageio.mimsave(gif_filename, images, duration=1)  

    """ Clean up the saved images """
    for filename in filenames:
        os.remove(filename)

data = pd.read_csv('GlobalLandTemperaturesByCity.csv')
data['Longitude'] = data['Longitude'].apply(convert_to_float)
data['Latitude'] = data['Latitude'].apply(convert_to_float)


tempandtime()
plt.show()
