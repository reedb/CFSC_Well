#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

'''
Created: Mon 26 Jul 2021 06:35:35 AM PDT

Read raw well time/date vs well bore height in feet data and plot.

Raw data format:
08-19-2015, 37.0

'''

DATA_FILE = "raw_well_level_data.txt"

with open(DATA_FILE, "r") as f:
    lines = f.readlines()


dates, levels = [], []
for line in lines:
    dats = line.split(',')
    if len(dats) >= 2:
        date, level = dats[:2]
        date = datetime.strptime(date, "%m-%d-%Y")
        level = float(level)
        dates.append(date)
        levels.append(level)

#plt.ylim([0, 70])
plt.xlabel("year")
plt.ylabel("well height, feet")
plt.scatter(dates, levels)
plt.scatter(dates[-1], levels[-1])
plt.show()
print("hit 'Enter'")

# all years taken together:
month_days = []
for date in dates:
    month_days.append(date.replace(year=2000))
fig, ax = plt.subplots(1)
#plt.ylim([0, 70])
plt.xlabel("date")
plt.ylabel("well height, feet")

plt.scatter(month_days, levels)
plt.scatter(month_days[-1], levels[-1])
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %d"))
plt.show()
print("hit 'Enter'")
