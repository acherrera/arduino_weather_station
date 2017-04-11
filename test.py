
import matplotlib.dates as mdate
import datetime
import matplotlib.pyplot as plt

# File path does not chagne for now
file_path = '/home/tony/Centered/weather_station/test_data/20170409_Meso.txt'


with open(file_path) as f:
    data = f.readlines()


""" Data of form: 
April 09 2017 00:00  64.1 64.1 64.1 73 2 144 6 12:00AM 29.571 0.00 0.29 0.29
74.0 44 0 0.0

Note: NOT CSV. use list.split(' ')

Now, what does it all mean?
Month, DD, YYYY, HH:MM, Temp1, Temp2, Temp3, Temp_inside, radiation?, Wind_dir,
no idea about the rest... plot it!
"""

times = []
data1 = []
data2 = []
data3 = []

# =================== Stripping Data ====================
for line in data:
    line = line.split(' ')

    # Time data ===========================
    valid = line[0:4]
    valid = '-'.join(valid)
    # April-09-2017-23:55
    valid = datetime.datetime.strptime(valid, "%B-%d-%Y-%H:%M")
    times.append(valid)

    # Stripping and figureing out data1-3
    first_var = line[5]
    second_var = line[6]
    third_var = line[7]

    data1.append(first_var)
    data2.append(second_var)
    data3.append(third_var)

def pair_data(time_in, var_in):
    x = []
    y = []
    for i in range(len(time_in)):
        try:
            variable_i = float(var_in[i])
            print(variable_i)
            time_i = time_in[i]
            x.append(time_i)
            y.append(variable_i)

        except:
            pass

    return x, y

# This seems to be working now
x1, y1 = pair_data(times, data1)

for i in range(len(x1)):
    print("{} ---- {}".format(x1[1], y1[i]))

# ===================== Plotting ========================

"""
title = 'testing'
xlabel = 'time'
ylabel = 'testing'

fig = plt.figure()
ax1 = plt.subplot(1, 1, 1)

x1, y1 = pair_data(times, data)
print(x1, y1)

ax1.plot(x1, y1)
plt.title(title)
plt.xlabel(xlabel)
plt.ylabel(ylabel)

xfmt = mdate.DateFormatter('%H:%M')
ax1.xaxis.set_major_formatter(xfmt)
fig.autofmt_xdate()

plt.show()

"""
