from django.shortcuts import render, redirect
from .models import Member, Kommando, Krieg, Sister, Xeno, Imperium, Chao, Kommand_list
from .forms import CreateUserForm, kommando_form
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect, FileResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

def home(request):
    return render(request, 'home.html', {})

def saved(request):
    all = Kommand_list.objects.all()
    return render(request, 'saved.html', {'all':all})

#LOGIN/LOGOUT
def login_user(request):
    if request.method == "POST":    
        username = request.POST['uname']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("Login Successful"))
            return redirect('home')
        else:
            messages.success(request, ("Login Failed, Please Try Again"))
            return redirect('login')
    else:
        return render(request, 'login.html', {})
    
def logout_user(request):
    logout(request)
    messages.success(request, ("Logged Out"))
    return redirect('home')

def create(request):
    if request.method =="POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, ("Sign Up Completed"))
            return redirect ('home')
    else:
        form = CreateUserForm()
        
    return render( request, 'create.html', {'form':form,})
    
#FACTION PAGE RENDERS   
def ork(request):
    o_form = kommando_form
    if request.method == "POST":
        o_form = kommando_form(request.POST)
        if o_form.is_valid():
            o_form.save()
            return render(request, 'ork.html', {'o_form':o_form})
        else:
            o_form = kommando_form
            return render(request, 'ork.html',{})
           
    nob = Kommando.objects.filter(unit = 'Kommando Nob')
    rokkit = Kommando.objects.filter(unit = 'Kommando Rokkit Boy')
    boy = Kommando.objects.filter(unit = 'Kommando Boy')
    return render(request, 'ork.html', {'nob':nob, 'rokkit':rokkit, 'boy':boy, 'o_form':o_form})

def sister(request):
    all_units = Sister.objects.all
    return render(request, 'sob.html', {'all':all_units})

def krieg(request):
    return render(request, 'krieg.html', {})


#FACTION NAVIGATION
def xeno(request):
    ork_kom = Xeno.objects.filter(Fac_name = 'Ork Kommando')
    tau = Xeno.objects.filter(Fac_name = 'Tau Pathfinders')
    eldar = Xeno.objects.filter(Fac_name = 'Eldar')
    nids = Xeno.objects.filter(Fac_name = 'Tyranids')
    return render(request, 'xeno.html', {'ork':ork_kom, 'tau':tau, 'eldar':eldar, 'nids':nids, })

def chaos(request):
    cm = Chao.objects.filter(Fac_name = 'Chaos')
    blood = Chao.objects.filter(Fac_name = 'Bloodied')
    dg = Chao.objects.filter(Fac_name = 'Death Guard')
    return render(request, 'chaos.html', {'cm':cm, 'blood':blood, 'dg':dg})

def imperium(request):
    sob = Imperium.objects.filter(Fac_name = 'Sisters of Battle')
    pm = Imperium.objects.filter(Fac_name = 'Primaris Marine')
    krieg = Imperium.objects.filter(Fac_name = 'Krieg')
    return render(request, 'imperium.html', {'sob':sob, 'pm':pm, 'krieg':krieg})


        