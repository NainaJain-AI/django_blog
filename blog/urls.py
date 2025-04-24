"""
URL Configuration for the blog app.

This module contains the URL patterns for the journal application,
mapping URLs to their corresponding view functions.
"""

from django.urls import path
from . import views

app_name = 'blog'  # Namespace for the app

urlpatterns = [
    # Main views
    path('', views.welcome, name='welcome'),  # Welcome/landing page
    
    # Journal entry views
    path('journal/', views.journal, name='journal'),  # List all entries
    path('journal/add/', views.add_entry, name='add_entry'),  # Add new entry
    path('journal/edit/<int:entry_id>/', views.edit_entry, name='edit_entry'),  # Edit existing entry
]
