"""rank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
"""
from random import choice

from django.urls import path
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from rank.api import api
from rank.base_views import test_page_for_templates
from applications.events.views import events_running, event_details, event_details_spec
from applications.accounts.views import login_view, logout_view


def generate_strange_url():
    """Generate a strange url for admin protection"""
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
    return ''.join(choice(chars) for _ in range(30))


urlpatterns = [
    path('admin/', admin.site.urls),

    # semantic-ui testing
    path('ranking/', test_page_for_templates, name='semantic_testing'),

    # events
    path('', events_running, name='events_running'),
    path('event_details/', event_details, name='event_details'),
    path('event_details/<int:event>/', event_details_spec, name='event_details_spec'),

    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    path('api/', api.urls),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)