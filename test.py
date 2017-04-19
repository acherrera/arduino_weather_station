
import matplotlib.dates as mdate
import datetime
import matplotlib.pyplot as plt

# File path does not chagne for now
file_location = \
'/home/tony/Centered/weather_station/test_data/20170414_Meso.txt'

def extract_meso(file_path):
    with open(file_path) as f:
        data = f.readlines()


    """ Data of form:
    April 09 2017 00:00  64.1 64.1 64.1 73 2 144 6 12:00AM 29.571 0.00 0.29 0.29
    74.0 44 0 0.0

    Note: NOT CSV. use list.split(' ')

    Now, what does it all mean?
    Month, DD, YYYY, HH:MM, Temp1, Temp2, Temp3, Temp_inside, radiation?, Wind_dir,
    no idea about the rest... plot it!

    Temp2, Temp3 have lots of the same values being returned - bad temps
    """

    times = []
    temp1 = []
    temp2 = []      # Long periods of const. value
    temp3 = []      # Long periods of const. value
    data4 = []      # Possible Temperature - between 60 and 80 fluctuations
    wind_spd = []   # Wind Speed
    wind_dir = []   # Wind direction
    data7 = []      # Limited data 8-24 throughout the day increase
    time2 = []      # does not plot
    pressure = []   # Pressure
    data10 = []     # possibly rainfall - all zeros on 04/09
    data11 = []     # 0.290 all day. No idea
    data12 = []     # 0.290 all day. No idea again
    data13 = []     # indoor temperature possibly
    data14 = []     # Indoor relative humidity
    solar_rad = []  # Solar radiation
    uv_index = []     # UV index

    # =================== Stripping Data ====================
    for line in data:
        line = line.split(' ')

        # Time data ===========================
        valid = line[0:4]           # Take time parts out
        valid = '-'.join(valid)     # Put back together 
        # April-09-2017-23:55
        valid = datetime.datetime.strptime(valid, "%B-%d-%Y-%H:%M") # Make object
        times.append(valid)

        # Stripping out temperature lines
        temp1.append(line[5])
        temp2.append(line[6])
        temp3.append(line[7])
        data4.append(line[8])
        wind_spd.append(line[9])
        wind_dir.append(line[10])
        data7.append(line[11])
        time2.append(line[12])
        pressure.append(line[13])
        data10.append(line[14])
        data11.append(line[15])
        data12.append(line[16])
        data13.append(line[17])
        data14.append(line[18])
        solar_rad.append(line[19])
        uv_index.append(line[20])

    return times, temp1, temp2, temp3, data4, wind_spd, wind_dir, data7, time2,\
    pressure, data10, data11, data12, data13, data14, solar_rad, uv_index

# This big lines records all the data from the mesonet sensor
times, temp1, temp2, temp3, data4, wind_spd, wind_dir, data7, time2, \
pressure, data10, data11, data12, data13, data14, \
solar_rad, uv_index  = extract_meso(file_location)

def pair_data(time_in, var_in):
    # Gets rid of data that is missing so data can be plotted
    x = []
    y = []
    for i in range(len(time_in)):
        try:
            current_var = float(var_in[i])
            current_time = time_in[i]
            x.append(current_time)
            y.append(current_var)

        except:
            pass

    return x, y

#plot = False
plot = True


"""
def float_conversion(list_in):
    for i in range(len(list_in)):
        list_in[i] = float(list_in[i])
    return list_in

wind_dir = float_conversion(wind_dir)
"""

def float_conversion(list_in):
    # Converts list to float. 
    for i in range(len(list_in)):
        list_in[i] = float(list_in[i])
    return list_in

plt.hist(float_conversion(wind_dir), bins=20)
plt.show()

"""
if plot:
    # ===================== Plotting ========================
    title = 'testing'
    xlabel = 'time'
    ylabel = 'testing'

    fig = plt.figure()
    ax1 = plt.subplot(1, 1, 1)

    # ax1.plot(times, temp1, linewidth=1)
    ax1.hist(temp1) # WHY IS THIS NOT WORKING!
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    xfmt = mdate.DateFormatter('%H:%M')
    ax1.xaxis.set_major_formatter(xfmt)
    fig.autofmt_xdate()

    plt.show()
"""
