import numpy as np
import matplotlib.pyplot as plt
import statistics
import datetime
import csv

today = datetime.date.today()
now = datetime.datetime.now()
filename = "GlobalTemperatures.csv"

open_file = open(filename)
file_parse = csv.DictReader(open_file)
counter = 0
temperatures = []
dates = []
for line in file_parse:
    print(line)
    if line["LandAverageTemperature"] == '':
        continue
    dt = datetime.datetime.strptime(line["dt"], "%Y-%m-%d")
    temp = float(line["LandAverageTemperature"])
    temperatures.append(temp)
    dates.append(dt)

n = 200
middletemperatures = []
middledates = dates[0:-n]
for i in range(len(temperatures) - n):
    tempseveger = []
    for j in range(n):
        tempseveger.append(temperatures[i + j])
    meanT = statistics.mean(tempseveger)
    middletemperatures.append(meanT)

ts = [d.timestamp() for d in dates]
coeficient = np.polyfit(x=ts,y=temperatures,deg=2)
xfit = []
yfit = []
for t in ts:
    yfit.append(coeficient[0]*t**2+coeficient[1]*t**1+coeficient[2]*t**0)
    xfit.append(datetime.datetime.fromtimestamp(t))
for i in range(200):
    t = ts[-1]+i*365*24*60*60
    yfit.append(coeficient[0] * t ** 2 + coeficient[1] * t ** 1 + coeficient[2] * t ** 0)
    xfit.append(datetime.datetime.fromtimestamp(t))


plt.title("Global temperatures in the past 300 years")
plt.xlabel("years")
plt.yticks(np.arange(-5, 20))
plt.grid()
plt.ylabel("°C")
plt.plot(dates, temperatures)
# plt.plot(middledates, middletemperatures)
plt.plot(xfit,yfit,"r")
plt.show()

yfit0 = [y-yfit[0]for y in yfit]
middletemperatures0 = [y-yfit[0]for y in middletemperatures]

plt.title("Global temperatures in the past 300 years")
plt.xlabel("years")
plt.yticks(np.arange(-5, 7))
plt.grid()
plt.ylabel("°C")
plt.plot(middledates, middletemperatures0)
plt.plot(xfit,yfit0,"r")
plt.show()
