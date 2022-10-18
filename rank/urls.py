"""rank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path

from rank.base_views import test_page_for_templates

from applications.accounts.views import login_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),

    # semantic-ui testing
    path('ranking/', test_page_for_templates, name='semantic_testing'),

    path('', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
