from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms 
from django.forms import ModelForm
from .models import Kommand_list


class CreateUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        
        fields = ('username', 'email', 'password1', 'password2',)
                 
    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

LEADER = [
    ('leader1','Kommando Nob W/ Power Klaw'),
    ('leader2','Kommando Nob W/ Big Choppa'),
]

BOYS = [
    ('kommando boy','Kommando Boy'),
    ('slasha boy','Kommando Slasha Boy'),
]
class kommando_form(ModelForm):
    class Meta:
        model = Kommand_list
        name = forms.CharField(max_length=100)
        
        fields = ('name', 'unit01', 'unit02', 'unit03', 'unit04', 'unit05', 'unit06', 'unit07', 'unit08', 'unit09', 'unit10',)
    
    def __init__(self, *args, **kwargs):
        super(kommando_form, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['unit01'].widget.attrs['class'] = 'form-control'
        self.fields['unit02'].widget.attrs['class'] = 'form-control'
        self.fields['unit03'].widget.attrs['class'] = 'form-control'
        self.fields['unit04'].widget.attrs['class'] = 'form-control'
        self.fields['unit05'].widget.attrs['class'] = 'form-control'
        self.fields['unit06'].widget.attrs['class'] = 'form-control'
        self.fields['unit07'].widget.attrs['class'] = 'form-control'
        self.fields['unit08'].widget.attrs['class'] = 'form-control'
        self.fields['unit09'].widget.attrs['class'] = 'form-control'
        self.fields['unit10'].widget.attrs['class'] = 'form-control'
    
        