# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 16:24:21 2018

@author: mob3f
"""
import pandas as pd
import matplotlib.pyplot as plt
import nltk
from math import pi

threshold = 20 

data = pd.read_csv('C:/Users/mob3f/Documents/Python Scripts/DrFirst/search_data.csv')
data.describe()#Describe our data
data['totalResults'] = pd.to_numeric(data.totalResults, errors='coerce')#parse this column to numeric and put NA in place of text
#Change timestamps to datetime format
data['requestDate'] = pd.to_datetime(data['requestDate'])
data['responseDate'] = pd.to_datetime(data['responseDate'])

data['requestDuration']= (data['responseDate']-data['requestDate']).astype('timedelta64[ms]')#Calculate excution time 

#Sort data by request time, this is similar to sorting by response time.
data = data.sort_values(by=['requestDate'])
  
#Looping through data and detecting unique requests (see report)      
window={}
results={}
for index, row in data.iterrows():  
    if not pd.isnull(row['request']):
        c_search=row['request'].lower()
        c_time=row['requestDate']
        if not window: #If window is empty, add the term to it
            window[c_search]=c_time
        else: 
            for key in list(window):
                key=key.lower()
                if (key in c_search) or (c_search in key) or nltk.edit_distance(c_search, key)<=3: #For each term, compare it with the previous terms in the window. Not that this can be improved by using a Jaccard_similarity_score
                    window[c_search] = window.pop(key)#If they are similiar, replace the term in the window and its corresponding time by the new term
                else:    
                     #If we didn't find a similiar word in the window
                    if (c_time-window[key]).total_seconds() > threshold: #If ther current term in the window has expired, move it from the window to the result dictionary 
                        results[window[key]]=key
                window[c_search]=c_time #add the new term to the dictionary
                        

results=pd.DataFrame(pd.Series(results,name='request'))#Parse the result dictionary to a pandas dataframe 
results.to_csv('C:/Users/mob3f/Documents/Python Scripts/DrFirst/search_data_users.csv')#Export results to a csv file
results.shape #number of request
results.request.unique().size #number of unique requests
results.request.groupby(results.request).count().nlargest(20).plot(kind='bar')# Plot top 20 requests

#Plot number of users over time 
fig,ax = plt.subplots()
results.request.groupby(results.index.date).count().plot(ax=ax,marker='D',color='green', linestyle='--')

#Plot number of users over hours of the day
count=results.request.groupby(results.index.hour).count()
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

