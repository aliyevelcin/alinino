from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from accounts.models import User

class RegisterForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control','placeholder':'Şifrə'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control','placeholder':'Şifrə təkrarı'
    }))
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'İstifadəçi adı'}),
            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Ad'}),
            'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Soyad'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'E-mail'}),
        }

class LoginForm(AuthenticationForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control','placeholder':'Şifrə'
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control','placeholder':'İstifadəçi adı'
    }))
    class Meta:
        model = User
        fields = ['username','password']
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'İstifadəçi adı'}),
            'password':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Şifrə'}),
        }