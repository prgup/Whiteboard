#url of app1
#from django.contrib import admin
from django.urls import path
from . import views

app_name = 'app1'
urlpatterns = [
	path('', views.home, name='home'),
	path('topics/', views.topics, name = 'topics'),
	path('topics/<int:topic_id>/', views.topic, name = 'topic'),
	path('add_topic/', views.add_topic, name= 'add_topic'),#to display the form we just created
	path('add_entry/<int:topic_id>/', views.add_entry, name = 'add_entry'),
	path('edit_entry/<int:entry_id>/', views.edit_entry, name  = 'edit_entry'),


    
]
