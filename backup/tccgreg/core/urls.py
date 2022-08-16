"""tccgreg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    # just a test using semantic-ui and vuejs
    path('testing/', TemplateView.as_view('checking_semantic.html'), name='checking_semantic'),
]
