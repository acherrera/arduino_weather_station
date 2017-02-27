


# method to strip out date information from the file name
filePath = 'datasets/weather_data/20170226_000000_morning_weather.TXT'

time_stamp = filePath.split('.')[0].split('/')[-1].split('_')

YMD = time_stamp[0]
HMS = time_stamp[1]

print(YMD)
print(HMS)
