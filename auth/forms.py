from django import forms

class CreateUsersForm(forms.Form):

    login = forms.CharField(widget=forms.TextInput, label='Введите имя')
    password = forms.CharField(widget=forms.PasswordInput, label='Введите пароль')
    conf_password = forms.CharField(widget=forms.PasswordInput, label='Введите пароль')

class LoginUseForm(forms.Form):
    login = forms.CharField(widget=forms.TextInput, label='Введите имя')
    password = forms.CharField(widget=forms.PasswordInput, label='Введите пароль')