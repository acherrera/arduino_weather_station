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
times, temperature, dew_point, rel_hum, dirct, mslp = parse_ASOS(official_file)

# Imported function that pairs matching data - lots of missing data
plot_times, plot_variable = pair_ASOS(times, mslp)

# =========================== Menu for what to plot =====================

# With data, create save path and title to give the functions

title = 'Test Plotting'

fig = plt.figure()  # This is the 'canvas' of the plot. Used later for changes

# Actually plotting the data - with labels and everything
ax1 = plt.subplot(1, 1, 1)
ax1.plot(plot_times, plot_variable, label='Official Data')

# this is what make the x-axis format correctly
xfmt = mdate.DateFormatter('%H:%M')
ax1.xaxis.set_major_formatter(xfmt)
fig.autofmt_xdate()

plt.title(title)
plt.ylabel('Test Plot')
plt.xlabel('Test Plot Time')

plt.legend()
plt.show()
