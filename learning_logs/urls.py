"""Defines url patterns for learning_logs."""

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Home page.
    path('', views.index, name='index'),

    # Show all topics.
    path('topics/', views.topics, name='topics'),

    #特定主题的详细页面
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    #添加新主题的页面
    path('new_topic/', views.new_topic, name='new_topic'),
    #添加内容的页面
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    #编辑内容的页面
    path('edit/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]