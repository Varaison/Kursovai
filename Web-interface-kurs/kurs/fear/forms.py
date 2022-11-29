from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Service
from django import forms


class ServiceForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'Категория не выбрана'

    class Meta:
        model = Service
        fields = ['name', 'content', 'photo', 'price', 'cat', 'slug']
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control text-bg-dark'}),
                   'content': forms.Textarea(attrs={'class': 'form-control text-bg-dark'}),
                   'photo': forms.FileInput(attrs={'class': 'form-control form-control-sm text-bg-dark'}),
                   'price': forms.NumberInput(attrs={'class': 'form-control text-bg-dark'}),
                   'cat': forms.Select(attrs={'class': 'form-control text-bg-dark'}),
                   'slug': forms.TextInput(attrs={'class': 'form-control text-bg-dark'}),
                   }


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control text-bg-dark'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control text-bg-dark'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control text-bg-dark'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-control text-bg-dark'}))
    first_name = forms.CharField(label='Имя', required=False, widget=forms.TextInput(attrs={'class': 'form-control text-bg-dark'}))
    last_name = forms.CharField(label='Фамилия', required=False, widget=forms.TextInput(attrs={'class': 'form-control text-bg-dark'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control text-bg-dark'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control text-bg-dark'}))