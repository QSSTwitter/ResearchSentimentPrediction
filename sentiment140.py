# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 19:28:29 2020

@author: Murtuza
"""

import pandas as pd
data = pd.read_csv('data_with_everything.csv')


import json
import requests
import statistics
api_url_base = 'http://www.sentiment140.com/api/classify?text='


list_of_sent_scores_mean=[]
list_of_sent_scores_median=[]
not_good=[]
for ind,rows in data.head(4).iterrows():
    print(ind)
    lst_of_tweets=eval(rows['selected_quotes'])
    list_of_sent_scores=[]
    
    for each_tweet in lst_of_tweets:
        api_url=api_url_base+each_tweet
        response = requests.get(api_url)
        if response.status_code == 200:
            try:
                res=json.loads(response.content.decode('utf-8'))
                pol=res['results']['polarity']
                list_of_sent_scores.append(pol)
            except:
                list_of_sent_scores.append(-1)
        else:
            list_of_sent_scores.append(-1)
    
    if -1 not in list_of_sent_scores:
        if len(list_of_sent_scores)==0:
            list_of_sent_scores_mean.append(2)
            list_of_sent_scores_median.append(2)
        else:
            list_of_sent_scores_mean.append(int(statistics.mean(list_of_sent_scores)))
            list_of_sent_scores_median.append(int(statistics.median(list_of_sent_scores)))
    
    
    else:
        while -1 in list_of_sent_scores: list_of_sent_scores.remove(-1)
        if len(list_of_sent_scores)==0:
            list_of_sent_scores_mean.append(2)
            list_of_sent_scores_median.append(2)
        else:
            list_of_sent_scores_mean.append(int(statistics.mean(list_of_sent_scores)))
            list_of_sent_scores_median.append(int(statistics.median(list_of_sent_scores)))
        not_good.append(rows['altmetric_id'])
        









