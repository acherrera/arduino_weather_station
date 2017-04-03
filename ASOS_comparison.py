"""
This is a script that will plot ASOS data vs recorded data.
"""

import tkinter as tk
from tkinter import filedialog

import datetime
import matplotlib.dates as mdate
import matplotlib.pyplot as plt

from modules.functions import *
from modules.menus import *

# ===================== ASOS file handling =========================

input("\nNext Screen is the official file input - any key to continue")

# This file has to be downloaded as a CSV file to work
# File location from user using pretty GUI
root = tk.Tk()                      # make it
root.withdraw()                     # how to
raw_path = filedialog.askopenfile() # what to
root.destroy()                      # get rid of

# This is needed to make the file path work correctly
official_file = raw_path.name

# One line to hide lots of code needed to parse data out
times, temperature, dew_point, rel_hum, dirct = parse_ASOS(official_file)

# Because of all missing data, have to remove missing data before plotting. Could leave missing data
# as 'M' but already have it replaced with None type, so I'm leaving it for now

# =========================== Menu for what to plot =====================

plot_times = []
plot_variable = []

# runs through the list by index rather than actual value so when it comes back with a value, both the value
# and associated time can be added to the list
for i in range(len(temperature)):
    if temperature[i] is not None:
        plot_variable.append((float(temperature[i]) - 32) / 1.8)
        plot_times.append(times[i])



# ================= Unofficial File Handling ==================

input("Next Screen is the unofficial file input - any key to continue")

# This file has to be downloaded as a CSV file to work
# File location from user using pretty GUI
root = tk.Tk()                      # make it
root.withdraw()                     # how to
raw_path = filedialog.askopenfile() # what to
root.destroy()                      # get rid of

# This is needed to make the file path work correctly
unofficial_file = raw_path.name

lines_to_scan = 40  # lines to scan for the first non-comment line

data_start = data_start(unofficial_file, lines_to_scan)

start_time = get_start(data_start)

print("Start time is: {}".format(start_time))

time, temperature, pressure, rel_hum = get_data(unofficial_file, start_time)


# With data, create save path and title to give the functions
save_path = "{}_comparison.png".format(unofficial_file.split('.')[0])
title = 'Data Comparison:' \
        '{}'.format(unofficial_file.split('.')[0].split('/')[-1])

fig = plt.figure()  # This is the 'canvas' of the plot. Used later for changes

# Actually plotting the data - with labels and everything
ax1 = plt.subplot(1, 1, 1)
ax1.plot(plot_times, plot_variable, label='Official Data')
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
