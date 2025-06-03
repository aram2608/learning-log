"""Defines URL patterns for learning_logs."""

from django.urls import path # needed to map URLs to views

from . import views

app_name = 'learning_logs' # helps Django distinguish this app from the others in the project
urlpatterns = [
    # Home Page
    path('', views.index, name='index'), # empty string for now to match the base URL
    # Page that shows all topics
    path('topics/', views.topics, name='topics'),
    # Detail page for a single topic
    path('topics/<int:topic_id>/', views.topic, name='topic')
]