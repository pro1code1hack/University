from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from Teachers.models import Teacher


class NewUserForm(UserCreationForm):  # Наследуемся от встроенного класса

    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        if commit:
            user.save()
        return user