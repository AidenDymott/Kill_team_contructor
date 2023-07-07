from django.shortcuts import render, redirect
from .models import Member, Home_media, Kommando, Krieg, Sister, Xeno, Imperium, Chao, Kommand_list, sister_list, Krieg_list, Pm_list, Cm_list, Bloodied_list, Dg_list, Eldarg_list, Pathfinder_list, Tyranid_list, Tau_p
from .forms import CreateUserForm, kommando_form, sister_form, krieg_form, pm_form, swarm_form, guardian_form, cm_form, dg_form, blood_form, tau_form
from django.http import HttpResponseRedirect, FileResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

def home(request):
    kt = Home_media.objects.filter(name = 'Kill Team')
    com = Home_media.objects.filter(name = 'Community')
    return render(request, 'home.html', {'kt':kt, 'com':com})

def saved(request):
    ork = Kommand_list.objects.all()
    sob = sister_list.objects.all()
    pm = Pm_list.objects.all()
    krieg = Krieg_list.objects.all()
    death = Dg_list.objects.all()
    cm = Cm_list.objects.all()
    blood = Bloodied_list.objects.all()
    edar = Eldarg_list.objects.all()
    ptau = Pathfinder_list.objects.all()
    swarm = Tyranid_list.objects.all()
    ptau = Pathfinder_list.objects.all()
    return render(request, 'saved.html', {'ork':ork, 'sob':sob, 'pm':pm, 'krieg':krieg, 'death':death, 'cm':cm, 'blood':blood, 'edar':edar, 'ptau':ptau, 'swarm':swarm, 'ptau':ptau})



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

#XENOS
def xeno(request):
    ork_kom = Xeno.objects.filter(Fac_name = 'Ork Kommando')
    tau = Xeno.objects.filter(Fac_name = 'Tau Pathfinders')
    eldar = Xeno.objects.filter(Fac_name = 'Eldar')
    nids = Xeno.objects.filter(Fac_name = 'Tyranids')
    return render(request, 'xeno.html', {'ork':ork_kom, 'tau':tau, 'eldar':eldar, 'nids':nids, })

#ORK KOMMANDO   
def ork(request):
    o_form = kommando_form
    if request.method == "POST":
        o_form = kommando_form(request.POST)
        if o_form.is_valid():
            o_form.save()
            return render(request, 'ork.html', {'o_form':o_form})
        else:
            o_form = kommando_form
            return render(request, 'ork.html',{'o_form':o_form})
  
    return render(request, 'ork.html', {'o_form':o_form})

def update_ork(request, list_id):
    o_list = Kommand_list.objects.get(pk=list_id)
    form = kommando_form(request.POST or None, instance = o_list )
    if form.is_valid():
        form.save()
        return redirect('saved')
    return render(request, 'update_ork.html', {'o_list':o_list, 'form':form})
    
def delete_ork(request, list_id):
    list = Kommand_list.objects.get(pk=list_id)
    list.delete()
    return redirect('saved')
    

#SWARM   
def swarm(request):
    ts_form = swarm_form
    if request.method == "POST":
        ts_form = swarm_form(request.POST)
        if ts_form.is_valid():
            ts_form.save()
            return render(request, 'swarm.html', {'ts_form':ts_form})
        else:
            ts_form = swarm_form
            return render(request, 'swarm.html',{'ts_form':ts_form})
  
    return render(request, 'swarm.html', {'ts_form':ts_form})

def update_swarm(request, list_id):
    list = Tyranid_list.objects.get(pk=list_id)
    form = swarm_form(request.POST or None, instance=list)
    if form.is_valid():
        form.save()
        return redirect('saved')
    return render(request, 'update_swarm.html', {'list':list,'form':form})


#Eldar G 
def guardian(request):
    ge_form = guardian_form
    if request.method == "POST":
        ge_form = guardian_form(request.POST)
        if ge_form.is_valid():
            ge_form.save()
            return render(request, 'guardian.html', {'ge_form':ge_form})
        else:
            ge_form = guardian_form
            return render(request, 'guardian.html',{'ge_form':ge_form})
  
    return render(request, 'guardian.html', {'ge_form':ge_form})

def update_guardian(request, list_id):
    list = Eldarg_list.objects.get(pk=list_id)
    form = guardian_form(request.POST or None, instance=list)
    if form.is_valid():
        form.save()
        return redirect('saved')
    return render(request, 'update_guardian.html', {'list':list,'form':form})

#PATHFINDERS
def ptau(request):
    form = tau_form
    if request.method == "POST":
        form = tau_form(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'ptau.html', {'form':form})
        else:
            ge_form = guardian_form
            return render(request, 'ptau.html',{'form':form})
  
    return render(request, 'ptau.html', {'form':form})

def update_tau(request, list_id):
    list = Pathfinder_list.objects.get(pk=list_id)
    form = tau_form(request.POST or None, instance=list)
    if form.is_valid():
        form.save()
        return redirect('saved')
    return render(request, 'update_tau.html', {'list':list,'form':form})
    


#CHAOS
def chaos(request):
    cm = Chao.objects.filter(Fac_name = 'Chaos Legionary')
    blood = Chao.objects.filter(Fac_name = 'Bloodied')
    dg = Chao.objects.filter(Fac_name = 'Death Guard')
    return render(request, 'chaos.html', {'cm':cm, 'blood':blood, 'dg':dg})

#CM
def cm(request):
    c_form = cm_form
    if request.method == "POST":
        c_form = cm_form(request.POST)
        if c_form.is_valid():
            c_form.save()
            return render(request, 'cm.html', {'c_form':c_form})
        else:
            c_form = cm_form
            return render(request, 'cm.html')
    
    return render(request, 'cm.html', {'c_form':c_form})

def update_cm(request, list_id):
    list = Cm_list.objects.get(pk=list_id)
    form = cm_form(request.POST or None, instance=list)
    if form.is_valid():
        form.save()
        return redirect('saved')
    return render(request, 'update_cm.html', {'list':list,'form':form})

#DEATHGUARD
def dg(request):
    d_form = dg_form
    if request.method == "POST":
        d_form = dg_form(request.POST)
        if d_form.is_valid():
            d_form.save()
            return render(request, 'dg.html', {'d_form':d_form})
        else:
            form = dg_form
            return render(request, 'dg.html')
    
    return render(request, 'dg.html', {'d_form':d_form})

def update_dg(request, list_id):
    list = Dg_list.objects.get(pk=list_id)
    form = dg_form(request.POST or None, instance=list)
    if form.is_valid():
        form.save()
        return redirect('saved')
    return render(request, 'update_dg.html', {'list':list,'form':form})

#BLOODIED
def bloodied(request):
    b_form = blood_form
    if request.method == "POST":
        b_form = blood_form(request.POST)
        if b_form.is_valid():
            b_form.save()
            return render(request, 'bloodied.html', {'b_form':b_form})
        else:
            b_form = blood_form
            return render(request, 'bloodied.html')
    
    return render(request, 'bloodied.html', {'b_form':b_form})

def update_bloodied(request, list_id):
    list = Bloodied_list.objects.get(pk=list_id)
    form = blood_form(request.POST or None, instance=list)
    if form.is_valid():
        form.save()
        return redirect('saved')
    return render(request, 'update_pm.html', {'list':list,'form':form})

#IMPERIUM
def imperium(request):
    sob = Imperium.objects.filter(Fac_name = 'Sisters of Battle')
    pm = Imperium.objects.filter(Fac_name = 'Primaris Marine')
    krieg = Imperium.objects.filter(Fac_name = 'Veteran Guardsman')
    return render(request, 'imperium.html', {'sob':sob, 'pm':pm, 'krieg':krieg})

#SISTERS OF BATTLE
def sister(request):
    s_form = sister_form
    if request.method == "POST":
        s_form = sister_form(request.POST)
        if s_form.is_valid():
            s_form.save()
            return render(request, 'sob.html', {'s_form':s_form})
        else:
            s_form = sister_form
            return render(request, 'sob.html')
    
    return render(request, 'sob.html', {'s_form':s_form})

def update_sister(request, list_id):
    s_list = sister_list.objects.get(pk=list_id)
    s_form = sister_form(request.POST or None, instance=s_list)
    if s_form.is_valid():
        s_form.save()
        return redirect('saved')
    return render(request, 'update_sister.html', {'s_list':s_list,'s_form':s_form})
    

#PM
def pm(request):
    p_form = pm_form
    if request.method == "POST":
        p_form = pm_form(request.POST)
        if p_form.is_valid():
            p_form.save()
            return render(request, 'pm.html', {'p_form':p_form})
        else:
            p_form = pm_form
            return render(request, 'pm.html')
    
    return render(request, 'pm.html', {'p_form':p_form})

def update_pm(request, list_id):
    list = Pm_list.objects.get(pk=list_id)
    form = pm_form(request.POST or None, instance=list)
    if form.is_valid():
        form.save()
        return redirect('saved')
    return render(request, 'update_pm.html', {'list':list,'form':form})

#KRIEG
def krieg(request):
    k_form = krieg_form
    if request.method == "POST":
        k_form = krieg_form(request.POST)
        if k_form.is_valid():
            k_form.save()
            return render(request, 'krieg.html', {'k_form':k_form})
        else:
            k_form = krieg_form
            return render(request, 'krieg.html')
        
    return render(request, 'krieg.html', {'k_form':k_form})

def update_krieg(request, list_id):
    list = Krieg_list.objects.get(pk=list_id)
    form = krieg_form(request.POST or None, instance=list)
    if form.is_valid():
        form.save()
        return redirect('saved')
    return render(request, 'update_krieg.html', {'list':list,'form':form})


# TAC OPS VIEWS
def infiltration(request):
    return render(request, 'infiltration.html', {})

def security(request):
    return render(request, 'security.html', {})

def seek(request):
    return render(request, 'seek.html', {})

def recon(request):
    return render(request, 'recon.html', {})



        