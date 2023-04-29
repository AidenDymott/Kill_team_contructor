from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms 
from django.forms import ModelForm
from .models import Kommand_list, sister_list, Krieg_list, Pm_list, Tyranid_list, Eldarg_list, Cm_list, Bloodied_list, Dg_list


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


#XENOS FORMS

#KOMMANDO LIST
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
        
#SWARM

class swarm_form(ModelForm):
    class Meta:
        model = Tyranid_list
        name = forms.CharField(max_length=100)       
        fields = ('name', 'unit01', 'unit02', 'unit03', 'unit04', 'unit05', 'unit06', 'unit07', 'unit08', 'unit09', 'unit10', 'unit11', 'unit12', 'unit13', 'unit14', 'unit15', 'unit16',)
    
    def __init__(self, *args, **kwargs):
        super(swarm_form, self).__init__(*args, **kwargs)
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
        self.fields['unit11'].widget.attrs['class'] = 'form-control'
        self.fields['unit12'].widget.attrs['class'] = 'form-control'
        self.fields['unit13'].widget.attrs['class'] = 'form-control'
        self.fields['unit14'].widget.attrs['class'] = 'form-control'
        self.fields['unit15'].widget.attrs['class'] = 'form-control'
        self.fields['unit16'].widget.attrs['class'] = 'form-control'
        
#ELDAR GUARDIAN LIST
class guardian_form(ModelForm):
    class Meta:
        model = Eldarg_list
        name = forms.CharField(max_length=100)       
        fields = ('name', 'unit01', 'unit02', 'unit03', 'unit04', 'unit05', 'unit06', 'unit07', 'unit08', 'unit09', 'unit10',)
    
    def __init__(self, *args, **kwargs):
        super(guardian_form, self).__init__(*args, **kwargs)
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

#IMPERIUN FORMS

#SISTERS OF BATTLE       
class sister_form(ModelForm):
    class Meta:
        model = sister_list
        name = forms.CharField(max_length=100)       
        fields = ('name', 'unit01', 'unit02', 'unit03', 'unit04', 'unit05', 'unit06', 'unit07', 'unit08', 'unit09', 'unit10',)
    
    def __init__(self, *args, **kwargs):
        super(sister_form, self).__init__(*args, **kwargs)
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

#Primaris Marines        
class pm_form(ModelForm):
    class Meta:
        model = Pm_list
        name = forms.CharField(max_length=100)       
        fields = ('name', 'unit01', 'unit02', 'unit03', 'unit04', 'unit05', 'unit06',)
    
    def __init__(self, *args, **kwargs):
        super(pm_form, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['unit01'].widget.attrs['class'] = 'form-control'
        self.fields['unit02'].widget.attrs['class'] = 'form-control'
        self.fields['unit03'].widget.attrs['class'] = 'form-control'
        self.fields['unit04'].widget.attrs['class'] = 'form-control'
        self.fields['unit05'].widget.attrs['class'] = 'form-control'
        self.fields['unit06'].widget.attrs['class'] = 'form-control'
        
#KRIEG
class krieg_form(ModelForm):
    class Meta:
        model = Krieg_list
        name = forms.CharField(max_length=100)       
        fields = ('name', 'unit01', 'unit02', 'unit03', 'unit04', 'unit05', 'unit06', 'unit07', 'unit08', 'unit09', 'unit10',)
    
    def __init__(self, *args, **kwargs):
        super(krieg_form, self).__init__(*args, **kwargs)
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
    
#CHAOS FORMS

#CM       
class cm_form(ModelForm):
    class Meta:
        model = Cm_list
        name = forms.CharField(max_length=100)       
        fields = ('name', 'unit01', 'unit02', 'unit03', 'unit04', 'unit05', 'unit06',)
    
    def __init__(self, *args, **kwargs):
        super(cm_form, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['unit01'].widget.attrs['class'] = 'form-control'
        self.fields['unit02'].widget.attrs['class'] = 'form-control'
        self.fields['unit03'].widget.attrs['class'] = 'form-control'
        self.fields['unit04'].widget.attrs['class'] = 'form-control'
        self.fields['unit05'].widget.attrs['class'] = 'form-control'
        self.fields['unit06'].widget.attrs['class'] = 'form-control'

#DEATH GUARD      
class dg_form(ModelForm):
    class Meta:
        model = Dg_list
        name = forms.CharField(max_length=100)       
        fields = ('name', 'unit01', 'unit02', 'unit03', 'unit04',)
    
    def __init__(self, *args, **kwargs):
        super(dg_form, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['unit01'].widget.attrs['class'] = 'form-control'
        self.fields['unit02'].widget.attrs['class'] = 'form-control'
        self.fields['unit03'].widget.attrs['class'] = 'form-control'
        self.fields['unit04'].widget.attrs['class'] = 'form-control'
        
#BLOODIED
class blood_form(ModelForm):
    class Meta:
        model = Bloodied_list
        name = forms.CharField(max_length=100)       
        fields = ('name', 'unit01', 'unit02', 'unit03', 'unit04', 'unit05', 'unit06', 'unit07', 'unit08', 'unit09', 'unit10', 'unit11', 'unit12', 'unit13', 'unit14',)
    
    def __init__(self, *args, **kwargs):
        super(blood_form, self).__init__(*args, **kwargs)
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
        self.fields['unit11'].widget.attrs['class'] = 'form-control'
        self.fields['unit12'].widget.attrs['class'] = 'form-control'
        self.fields['unit13'].widget.attrs['class'] = 'form-control'
        self.fields['unit14'].widget.attrs['class'] = 'form-control'