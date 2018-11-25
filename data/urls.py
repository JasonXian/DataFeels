from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recommend/<topic>', views.recommend, name='recommend'),
    path('graph/<topic>', views.graph, name='graph'),
]