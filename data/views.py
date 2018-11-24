from django.shortcuts import render
from django.http import HttpResponse
from random import randint
from copy import deepcopy

seed = [
        {
            'url' : "https://www.google.ca",
            'title' : "article 1",
            'author' : "jason xian",
            'date' : "today",
            'topic' : "topic1",
            "summary" : "some random text",
            'sentiment_score' : 0.3,
            'thumbnail' : "https://pbs.twimg.com/profile_images/832456134292180992/k_PQ_FYi_400x400.jpg"
        },
        {
            'url' : "https://www.yahoo.ca",
            'title' : "article 2",
            'author' : "bryan au",
            'date' : "today",
            'topic' : "topic1",
            "summary" : "some random text",
            'sentiment_score' : 0.7,
            'thumbnail' : "https://pbs.twimg.com/profile_images/832456134292180992/k_PQ_FYi_400x400.jpg"
        },
    ]

data = []

for i in range(0, 50):
    base = deepcopy(seed[randint(0, 1)])
    score = randint(0,100) / 100
    base["sentiment_score"] = score
    base["title"] = "article " + str(i)
    data.append(base)

dummyData = {
    'topic1' : {
        'data' : {
            'topic': 'topic1',
            'high' : data[6:9],
            'average' : data[3:6],
            'low': data[0:3],
            'all': data
        }
    },
    'topic2' : {
        'data' : {
            'topic': 'topic2',
            'high' : data[15:18],
            'average' : data[12:15],
            'low': data[9:12],
            'all' : data,
        }
    }
}

def index(request):
    context = {'latest_question_list': ["1","2","3"]}
    return render(request, 'data/index.html', context)

def recommend(request, topic):
    context = dummyData[topic]
    return render(request, 'data/recommend.html', context)

def graph(request, topic):
    sortedArr = [[0 for col in range(20)] for row in range(10)]
    for article in dummyData[topic]['data']['all']:
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
    return render(request, 'data/graph.html', context)