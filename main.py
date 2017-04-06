"""
Created by Anthony Herrera to analyze Arduino weather station data.

WHEN RUN: will need to hit enter in the command prompt area and/or set the desired starting time. Program
will wait until you tell it when you want it to start. Keep hitting enter to start at start time of data.

"""

# TODO add temperature conversion availability. Need to update graph axis labels
# TODO add functionality for end time


# Time comes in form %04d%02d%02d_%02d%02d%02d - Because I made it that way.
# Data is of form: Time, Temperature, Pressure, Relative Humidity.


#===================== Importing Modules============================

import tkinter as tk
from tkinter import filedialog
import numpy as np

# custom modules - should be in file.
from modules.functions import *
from modules.graph_options import *
from modules.menus import *

# Use this to change the style of graph
plt.style.use('seaborn-notebook')


# =================== All the file handling ==========================

input("Choose .txt to use for data - press any key to continue")

# File location from user using pretty GUI
root = tk.Tk()                      # make it
root.withdraw()                     # how to
raw_path = filedialog.askopenfile() # what to
root.destroy()                      # get rid of

# This is needed to make the file path work correctly
file_path = raw_path.name

# Make sure the filename looks correct
print("\n")
print("File name is: {}".format(file_path.split('/')[-1]))


# Number of lines to scan for first non-commented line. Use to get the data
# start time and allow for comments at the beginning of files
lines_to_scan = 40
data_begin = data_start(file_path, lines_to_scan) # data_start is cutom function

# Imported function that runs through and get information from user. See modules
# file for more information
start_time = get_start(data_begin)

print("Start time is: {}".format(start_time))

# get_data is in moldules/functions.py file. This is what extracts the
# data given the input file
time, temperature, pressure, rel_hum = get_data(file_path, start_time)

# Reduce pressure to sea level
"""         P_sl = P*exp((z*g)/(R*T))
            P_sl: sea level pressure
            P: station pressure
            z: height MSL
            g: gravity
            R: 287
            T: temperature in Kelvin    """
for i in range(len(pressure)):
    pressure_value = pressure[i]
    z_MSL = 288.036     # MSL of KAMW airport in meters
    gravity = 9.81      # force of gravity
    R_gas = 287             # gas constant
    Temp_Kelvin = temperature[i] + 273.15
    SL_pressure = pressure_value*(np.exp((z_MSL*gravity)/(R_gas*Temp_Kelvin)))
    pressure[i] = SL_pressure # change value at index to sea level pressure



# ========== Plotting Menu. Get user input for plotting ===============

# Could add options for different graph layouts. 
plot_options = [("Temperature", 1),
                ("Pressure", 2),
                ("Relative Humidity", 3),
                ("Plot all", 4),
                ("Plot and save all of the above", 5),
                ("ASOS Comparison", 6)]

user_selection = menu_maker(plot_options)

if user_selection == 1:
    save_path = "{}_temperature.png".format(file_path.split('.')[0])
    title_string = 'Temperature for:' \
        '{}'.format(file_path.split('.')[0].split('/')[-1])
    single_plot(time, temperature, title_string, 'time', 'temperature(C)', save_path)


elif user_selection == 2:
    save_path = "{}_pressure.png".format(file_path.split('.')[0])
    title_string = 'pressure for:'\
        '{}'.format(file_path.split('.')[0].split('/')[-1])
    single_plot(time, pressure, title_string, 'time', 'pressure(hPa)', save_path)

elif user_selection == 3:
    save_path = "{}_RH.png".format(file_path.split('.')[0])
    title_string = 'RH for: {}'.format(file_path.split('.')[0].split('/')[-1])
    single_plot(time, rel_hum, title_string, 'time', 'Relavitve Humidity', save_path)

elif user_selection == 4:

    # With data, create save path and title to give the functions
    save_path = "{}_all.png".format(file_path.split('.')[0])
    title = 'All Data: {}'.format(file_path.split('.')[0].split('/')[-1])

    # This monster makes the three plots
    three_plots(x=time,
                y1=temperature,
                y2=pressure,
                y3=rel_hum,
                title=title,
                xlabel='time',
                ylabel1='Temperature (C)',
                ylabel2='Pressure (hPa)',
                ylabel3='RH (%)',
                save_file=save_path)

elif user_selection == 5:

    # Temperature Plotting
    save_path = "{}_temperature.png".format(file_path.split('.')[0])
    title_string = 'Temperature for:' \
        '{}'.format(file_path.split('.')[0].split('/')[-1])
    single_plot(time, temperature, title_string, 'time', 'temperature(C)', save_path)

    # Pressure Plotting
    save_path = "{}_pressure.png".format(file_path.split('.')[0])
    title_string = 'pressure for:'\
        '{}'.format(file_path.split('.')[0].split('/')[-1])
    single_plot(time, pressure, title_string, 'time', 'pressure(hPa)', save_path)

    # Relative Humidity plotting
    save_path = "{}_RH.png".format(file_path.split('.')[0])
    title_string = 'RH for: {}'.format(file_path.split('.')[0].split('/')[-1])
    single_plot(time, rel_hum, title_string, 'time', 'Relavitve Humidity', save_path)


    # Plotting them all
    save_path = "{}_all.png".format(file_path.split('.')[0])
    title = 'All Data: {}'.format(file_path.split('.')[0].split('/')[-1])

    # This monster makes the three plots
    three_plots(x=time,
                y1=temperature,
                y2=pressure,
                y3=rel_hum,
                title=title,
                xlabel='time',
                ylabel1='Temperature (C)',
                ylabel2='Pressure (hPa)',
                ylabel3='RH (%)',
                save_file=save_path)

# ====================== ASOS Comparison Handling ============================

elif user_selection == 6:
    input("\nNext Screen is the official file input - any key to continue")

    root = tk.Tk()                      # make it
    root.withdraw()                     # how to
    raw_path = filedialog.askopenfile() # what to
    root.destroy()                      # get rid of

    # This is needed to make the file path work correctly
    official_file = raw_path.name

    # appended "_ASOS" to data names to avoid potential conflicts
    times_ASOS, temperature_ASOS, dew_point_ASOS, rel_hum_ASOS, dirct,\
    ASOS_mslp= parse_ASOS(official_file)

    print("\nASOS data loaded\nWhat would you like to compare?")

    # Creating secondary menu for more user input
    ASOS_menu = [("Temperature", 1),
                 ("Pressure",2),
                 ("Relative Humidity",3),
                 ("Plot and save all of the above", 4)]


    ASOS_selection = menu_maker(ASOS_menu)

    if ASOS_selection == 1:

        # Temperature comparison - NOTE: ASOS data is in F
        x_plot, y_plot = pair_ASOS(times_ASOS, temperature_ASOS)
        y_plot = [((x-32)/1.8) for x in y_plot] #x is dummy variable. != x_plot

        # With data, create save path and title to give the functions
        save_path = "{}_temperature_comparison.png".format(file_path.split('.')[0])
        title = 'Temperature Comparison:' \
                '{}'.format(file_path.split('.')[0].split('/')[-1])

        fig = plt.figure()  # This is the 'canvas' of the plot. Used later for changes

        # Actually plotting the data - with labels and everything
        ax1 = plt.subplot(1, 1, 1)
        ax1.plot(x_plot, y_plot, label='Official Data')
        ax1.plot(time, temperature, label='unofficial data')

        # this is what make the x-axis format correctly
        xfmt = mdate.DateFormatter('%H:%M')
        ax1.xaxis.set_major_formatter(xfmt)
        fig.autofmt_xdate()

        plt.title(title)
        plt.ylabel('Temperature(C)')
        plt.xlabel('Time (Hour:Minutes)')

        plt.legend()
        plt.savefig(save_path)
        plt.show()

    if ASOS_selection == 2:
        # Pressure comparison: ASOS is sea level pressure
        """
        # P_sl = P*exp((z*g)/(R*T))
            P_sl: sea level pressure
            P: station pressure
            z: height MSL
            g: gravity
            R: 287
            T: temperature in Kelvin
        """
        print(2)



    if ASOS_selection == 3:
        # Relative Humidity comparison
        print(3)

    if ASOS_selection == 4:
        # All of the above
        print(4)

"""
time, temperature, pressure, rel_hum = get_data(file_path, start_time)
"""
