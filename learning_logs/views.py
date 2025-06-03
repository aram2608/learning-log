from django.shortcuts import render
from .models import Topic

def index(request):
    """The home page for Learning Log."""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """The topics page for the Learning Logs."""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics} # a context is a dictionary in which keys are names well use in the template to access data we want, and the values are data we want to send
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id): # this parameter gets captured by /<int:topic_id>/
    """Show a single topic and all its entries."""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)