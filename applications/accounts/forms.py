from django.contrib.auth.forms import UserCreationForm

from .models import Profile


class ProfileCreationForm(UserCreationForm):
    class Meta:
        model = Profile
        fields = ['name', 'username', 'user_type']