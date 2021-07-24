# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 21:20:05 2020

@author: Murtuza
"""

from sentistrength import PySentiStr
senti = PySentiStr()
SentiStrengthLocation = "C:/SentStrength_Data/SentiStrength.jar" #The location of SentiStrength on your computer
SentiStrengthLanguageFolder = "C:\SentStrength_Data\SentStrength_Data_Sept2011/" #The location of the unzipped SentiStrength data files on your computer

senti.setSentiStrengthPath(SentiStrengthLocation)
senti.setSentiStrengthLanguageFolderPath(SentiStrengthLanguageFolder)


import pandas as pd
data = pd.read_csv('data_with_everything.csv')

import statistics
list_of_sent_scores_mean=[]
list_of_sent_scores_median=[]

for ind,rows in data.iterrows():
    print(ind)
    lst_of_tweets=eval(rows['selected_quotes'])
    list_of_sent_scores=[]
    result = senti.getSentiment(lst_of_tweets,score='trinary')
    for val in result:
        list_of_sent_scores.append(val[2])
    list_of_sent_scores_mean.append(int(statistics.mean(list_of_sent_scores)))
    list_of_sent_scores_median.append(int(statistics.median(list_of_sent_scores)))


from collections import Counter
Counter(list_of_sent_scores_mean)
# Counter({0: 106057, -1: 31212, 1: 11443})

Counter(list_of_sent_scores_median)
# Counter({0: 94716, -1: 39091, 1: 14905})