from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {'latest_question_list': ["1","2","3"]}
    return render(request, 'data/index.html', context)

def recommend(request, topic):
    return HttpResponse("You're looking at question %s." % topic)

def graph(request, topic):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % topic)