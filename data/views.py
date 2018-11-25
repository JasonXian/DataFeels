from django.shortcuts import render
from django.http import HttpResponse
from random import randint
from copy import deepcopy
import os
import pandas as pd

module_dir = os.path.dirname(__file__)
file_path = os.path.join(module_dir, 'file.csv')
df = pd.read_csv(file_path)
cryptoData = df.to_dict(orient='records')
cryptoData = sorted(cryptoData, key = lambda k: k['sentiment_score'])

"""
article dict structure for reference
'data' : {
    'emotion' : {},
    'keywords' : {},
    'personality' : {},
    'sentiment_hq_score': 0,
    'sentiment_score' : 0,
    'source': '',
    'summarization' : '',
    'title' : '',
    'url' : '',
    'thumbnail': ''
}
"""

def recommendify(data, topic):
    minIndex = 0
    minVal = 10
    for i in range(len(data)):
        if abs(data[i]['sentiment_score'] - 0.5) < minVal :
            minIndex = i
            minVal = abs(data[i]['sentiment_score'] - 0.5)
    highAvg = round((len(data) + minIndex) / 2)
    lowAvg = round(minIndex / 2)
    returnData = {
        'topic' : topic,
        'high' : data[highAvg - 1: highAvg + 2],
        'average' : data[minIndex - 1: minIndex + 2],
        'low' : data[lowAvg - 1: lowAvg + 2]
    }
    return returnData

def graphify(data, topic):
    sortedArr = [[0 for col in range(20)] for row in range(10)]
    for article in data:
        index = round(article['sentiment_score'] * 20)
        if index == 20:
            index = 19
        for row in sortedArr:
            if row[index] == 0:
                row[index] = article 
                break
    sortedArr.reverse()
    context = {
        'topic' : topic,
        'sorted' : sortedArr,
    }
    return context

data = {
    'cryptocurrency' : {
        'recommend': recommendify(cryptoData, 'cryptocurrency'),
        'graph' : graphify(cryptoData, 'cryptocurrency'),
    },
}

def index(request):
    return render(request, 'data/index.html', {})

def recommend(request, topic):
    return render(request, 'data/recommend.html', data[topic]['recommend'])

def graph(request, topic):
    return render(request, 'data/graph.html', data[topic]['graph'])