"""
Created by Anthony Herrera to analyze Arduino weather station data.

"""
# TODO convert timestamp to UNIX time or a useable date time stamp for graphing
""" Try something like this for the converstion
import datetime
import time

print datetime.datetime(2003, 8, 4, 21, 41, 43)"""
# Time comes in form %04d%02d%02d_%02d%02d%02d - Because I made it that way.


import matplotlib.pyplot as plt

data = []
with open('DATALOG.TXT') as f:
    data = f.readlines()

temp = []
pressure = []
rel_hum = []

# This is used because I'm not sure of the final data output form
start_index = 1

for line in data:
    temp.append(float(line.split(',')[start_index]))
    pressure.append(float(line.split(',')[start_index + 1]))
    rel_hum.append(float(line.split(',')[start_index + 2]))

x = [i for i in range(len(temp))]


fig, ax1 = plt.subplots()
ax1.plot(x, temp, 'b-')
ax1.set_xlabel('time (not really)')
# Make the y-axis label, ticks and tick labels match the line color.
ax1.set_ylabel('Temperature', color='b')
ax1.tick_params('y', colors='b')

ax2 = ax1.twinx()
ax2.plot(x, rel_hum, 'r-')
ax2.set_ylabel('Relative Humidity', color='r')
ax2.tick_params('y', colors='r')

fig.tight_layout()
plt.show()

plt.show()


""" Dumb Anthony way of plotting data
plt.subplot(2, 1 ,1)
plt.plot(x, temp)
plt.xlabel('Time - not really')
plt.ylabel('Temp')

plt.subplot(2, 1 ,2)
plt.plot(x, pressure)
plt.xlabel('Time - not really')
plt.ylabel('Pressure')
"""