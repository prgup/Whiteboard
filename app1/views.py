'''
Views are Python functions that receive an HttpRequest object 
and returns an HttpResponse object. 

Receive a request as a parameter and returns a response as a result. 
'''

from django.shortcuts import render, redirect

from .models import Topic, Entry
from .forms import TitleForm, ContentForm
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

def add_topic(request):
	if request.method != 'POST':
		form = TitleForm()
	else:
		#if post data submitted
		form = TitleForm(data=request.POST)
		if form.is_valid():
			form.save()
			return redirect('app1:topics')

	context= {'form': form}
	return render(request, 'app1/add_topic.html', context)
	
def add_entry(request, topic_id):
	topic = Topic.objects.get(id = topic_id)

	if request.method != 'POST':
		form = ContentForm()

	else:
		form = ContentForm(data = request.POST)
		if form.is_valid():
			add_entry = form.save(commit = False)
			add_entry.topic = topic
			add_entry.save()
			return redirect('app1:topic', topic_id = topic_id)
	
	context = {'topic': topic, 'form': form}
	return render(request, 'app1/add_entry.html', context)


def edit_entry(request, entry_id):
	entry = Entry.objects.get(id =entry_id)
	topic = entry.topic

	if request.method != 'POST':
		form = ContentForm(instance = entry)
	else:
		form = ContentForm(instance=entry, data=request.POST)
		if form.is_valid:
			form.save()
			return redirect('app1:topic', topic_id = topic.id)
	context  = {'entry': entry, 'topic': topic, 'form': form}
	return render(request, 'app1/edit_entry.html', context)



