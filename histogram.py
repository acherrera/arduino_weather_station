import matplotlib.pyplot as plt
import matplotlib.dates as mdate
import datetime

fileName = '20170223_124200.txt'

data = []
with open('20170223_124200.txt') as f:
    data = f.readlines()

time = []
temp = []
pressure = []
rel_hum = []

start_index = 0

for line in data:

    time_data = str(line.split(',')[0])
    year = int(time_data[0:4])
    month = int(time_data[4:6])
    day = int(time_data[6:8])
    hour = int(time_data[9:11])
    minute = int(time_data[11:13])
    second = int(time_data[13:15])

    time.append(datetime.datetime(year,month,day,hour,minute, second))

    temp.append(float(line.split(',')[1]))
    pressure.append(float(line.split(',')[2]))
    rel_hum.append(float(line.split(',')[3]))

plt.hist(time, )

plt.show()