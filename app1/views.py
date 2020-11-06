from django.shortcuts import render

from .models import Topic
# Create your views here.
def home(request):
	return render(request, 'app1/home.html')
def topics(request):
	topics = Topic.objects.order_by('date_added')
	context = {'topics': topics}
	return render(request, 'app1/topics.html', context)

def topic(request, topic_id):
	topic = Topic.objects.get(id=topic_id)
	entries = topic.entry_set.order_by('-date_added')
	context = {'topic': topic, 'entries': entries}
	return render(request, 'app1/topic.html', context)