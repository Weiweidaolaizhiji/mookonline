from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(required=True, min_length=3)
    password = forms.CharField(required=True, min_length=3)


class RegisterForm(forms.Form):
    mobile = forms.CharField(required=True, max_length=11)
    password = forms.CharField(required=True)
