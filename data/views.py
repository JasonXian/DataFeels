from django.shortcuts import render
from django.http import HttpResponse

data = [
        {
            'url' : "https://www.google.ca",
            'title' : "article 1",
            'author' : "jason xian",
            'date' : "today",
            'topic' : "topic1",
            "summary" : "some random text",
            'sentiment_value' : 0.3,
            'thumbnail' : "https://pbs.twimg.com/profile_images/832456134292180992/k_PQ_FYi_400x400.jpg"
        },
        {
            'url' : "https://www.yahoo.ca",
            'title' : "article 2",
            'author' : "bryan au",
            'date' : "today",
            'topic' : "topic1",
            "summary" : "some random text",
            'sentiment_value' : 0.7,
            'thumbnail' : "https://pbs.twimg.com/profile_images/832456134292180992/k_PQ_FYi_400x400.jpg"
        },
    ]

dummyData = {
    'topic1' : {
        'data' : {
            'topic': 'topic1',
            'high' : data,
            'average' : data,
            'low': data
        }
    },
    'topic2' : {
        'data' : {
            'topic': 'topic2',
            'high' : data,
            'average' : data,
            'low' : data
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
    context = dummyData[topic]
    return render(request, 'data/graph.html', context)