#url of app1
#from django.contrib import admin
from django.urls import path
from . import views

app_name = 'app1'
urlpatterns = [
	path('', views.home, name='home'),
	path('topics/', views.topics, name = 'topics'),
	path('topics/(?P<topic_id>\d+)/', views.topic, name = 'topic'),

    
]
