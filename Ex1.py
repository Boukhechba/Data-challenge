# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 12:13:27 2018

@author: mob3f
"""

import pandas as pd
import matplotlib.pyplot as plt
from math import pi
from matplotlib import rcParams



data = pd.read_csv('C:/Users/mob3f/Documents/Python Scripts/DrFirst/search_data.csv')
#

#Parse totalResults to numeric, any string will be replaced by NA
data['totalResults'] = pd.to_numeric(data.totalResults, errors='coerce')

#Change timestamps to datetime format
data['requestDate'] = pd.to_datetime(data['requestDate'])
data['responseDate'] = pd.to_datetime(data['responseDate'])
#Calculate excution time 
data['requestDuration']= (data['responseDate']-data['requestDate']).astype('timedelta64[ms]')
#Sort data by request time, this is similar to sorting by response time.
data = data.sort_values(by=['requestDate'])


#Calculate correlation between our variables
data['totalResults'].corr(data['requestDuration'])
data['responseSize'].corr(data['requestDuration'])

# Plot box plots for numeric columns 
rcParams['xtick.labelsize'] = 10
rcParams['ytick.labelsize'] = 16

fig,ax = plt.subplots(nrows=4, ncols=1)
boxprops = dict(linestyle='--', linewidth=3, color='darkgoldenrod')
flierprops = dict(marker='o', markerfacecolor='green', markersize=12,linestyle='none')
medianprops = dict(linestyle='-', linewidth=3.5, color='firebrick')
meanpointprops = dict(marker='D', markeredgecolor='black',markerfacecolor='firebrick')
meanlineprops = dict(linestyle='--', linewidth=2.5, color='purple')

data.boxplot(ax=ax[0],column='totalResults',vert=False,boxprops=boxprops, medianprops=medianprops, showfliers=False, showmeans=True)
data.boxplot(ax=ax[1],column='requestDuration',boxprops=boxprops,vert=False, medianprops=medianprops, showfliers=False, showmeans=True)
data.boxplot(ax=ax[2],column='responseSize',boxprops=boxprops,vert=False, medianprops=medianprops, showfliers=False, showmeans=True)
data.boxplot(ax=ax[3],column='requestSize',boxprops=boxprops,vert=False, medianprops=medianprops, showfliers=False, showmeans=True)

#some descriptive stats
data.request.unique().size #number of unique requests
data.loc[data.totalResults==0].shape[0]/data.shape[0]
data.loc[data.totalResults<2].shape[0]/data.shape[0]

#Export a descriptive table to csv 
tab=data.describe()
tab.to_csv('C:/Users/mob3f/Documents/Python Scripts/DrFirst/data_describe.csv')
#Plot number of requests over days
fig,ax = plt.subplots()
data.requestDate.groupby(data.requestDate.dt.date).count().plot(ax=ax,marker='D',color='green', linestyle='--')

#Plot number of requests over time of day
count=data.requestDate.groupby(data.requestDate.dt.hour).count()
categories=count.keys()
N = len(categories)
# What will be the angle of each axis in the plot? (we divide the plot / number of variable)
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]
# Initialise the spider plot
ax = plt.subplot(111,polar=True)
# If you want the first axis to be on top:
ax.set_theta_offset(pi / 2)
ax.set_theta_direction(-1) 
# Draw one axe per hour + add labels 
plt.xticks(angles[:-1], categories) 
# Draw ylabels
ax.set_rlabel_position(0)
ax.plot(angles[:-1], count, linewidth=2.5,color='green', linestyle='--', label="number of requests")
ax.fill(angles[:-1], count, 'b', alpha=0.2)

