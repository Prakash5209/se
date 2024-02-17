from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm

from .models import User,ProfileDetail

class AuthenticateForm(AuthenticationForm):
    pass

    def __init__(self,*args,**kwargs):
        super().__init__(self,*args,**kwargs)
        for i in self.fields:
            self.fields[i].widget.attrs.update({'class':'form-control'})

    
class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','password1','password2',)

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for i in self.fields:
            self.fields[i].widget.attrs.update({'class':'form-control'})


class ProfileDetailiForm(forms.ModelForm):
    class Meta:
        model = ProfileDetail
        # fields = '__all__'
        exclude = ('user',)
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for i in self.fields:
            self.fields[i].widget.attrs.update({'class':'form-control'})

    

