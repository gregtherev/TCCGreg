from django.contrib import admin

from .models import Profile
from .forms import ProfileCreationForm

class ProfileCreation(admin.ModelAdmin):
    form = ProfileCreationForm


admin.site.register(Profile, ProfileCreation)
