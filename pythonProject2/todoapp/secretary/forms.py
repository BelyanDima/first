from django import forms
from .models import Executor, ToDo
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                       'autocomplete': 'off'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                                  'autocomplete': 'off'}))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                                            'autocomplete': 'off'}))
    email = forms.CharField(label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-control',
                                                                           'autocomplete': 'off'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                       'autocomplete': 'off'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ['title', 'executor', 'period_of_execution', 'is_complete']

        widgets = {
            'title': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'executor': forms.Select(attrs={'class': 'form-control'}),
            'period_of_execution': forms.DateInput()
        }
