"""rank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path

# just for semantic-ui and vuejs test
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),

    # semantic-ui testing
    path('semantic_testing/',
         TemplateView.as_view(template_name='checking_semantic.html'),
         name='semantic_testing'),
]
