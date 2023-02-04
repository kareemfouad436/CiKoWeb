from django.shortcuts import render, redirect 
from django.http import HttpResponse

from .models import contact
from .forms import add_playerform

from .models import *
from .forms import *

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import *




@unauthenticated_user
def loginpage1(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password )
        if user is not None:
            login(request, user)
            return redirect('/')
        else:

            messages.error(request, 'Usernamr or Password is incorrect')
    context = {}
    return render(request, 'from/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')






@login_required(login_url='login')
@admin_only
def player(request):
    contacts = contact.objects.all()
    return render(request, 'from/contact.html', {'contacts':contacts})

@login_required(login_url='login')
def passport(request):
    return render(request, 'from/passport.html')

@login_required(login_url='login')
def music (request):
    return render(request, 'from/music.html') 

@login_required(login_url='login')
def travel (request):
    return render(request, 'from/travel.html') 

@login_required(login_url='login')
def national_anthem (request):
    return render(request, 'from/national_anthem.html') 
    
@login_required(login_url='login')
def createOrder(request):
    context = {}
    return render(request, 'from/create_update.html', context) 
    
    
    
 
 

 
 
@login_required(login_url='login')
def home(request):
    users = username.objects.all()
    palyers_count = users.count()
    context = {'users':users, 'palyers_count':palyers_count}
    return render(request, 'from/index.html', {'users':users})

##@login_required(login_url='login')
##def home_phone(request):
##    home_phone = UserProfile.objects.get(id=pk)
##    form = add_homeform (instance=update_homeform)
##    if request.method=='POST':
##        form = add_homeform (request.POST, instance=update_homeform)
##        if form.is_valid():
##            form.save()
##            return redirect('/')	
##    else:
##        pass
##    context = {'form':form}
##    return render(request, 'from/update_player.html', context)

@login_required(login_url='login') 
def add_player (request):
    form = add_playerform()
    if request.method=='POST':
        form = add_playerform (request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.UserProfile = request.user
            instance.save()
            ##form.save()
            return redirect('/contact')	
    else:
        pass
    context = {'form': form}
    return render(request, 'from/add_player.html', context)

@login_required(login_url='login')    
def update_player (request, pk):
    update_player = contact.objects.get(id=pk)
    form = add_playerform (instance=update_player)
    if request.method=='POST':
        form = add_playerform (request.POST, instance=update_player)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.UserProfile = request.user
            instance.save()
            ##form.save()
            return redirect('/contact')	
    else:
        pass
    context = {'form':form}
    return render(request, 'from/update_player.html', context)

@login_required(login_url='login')    
def delete_player (request, player_id):
    i = contact.objects.get(pk=player_id)
    i.delete()
    return redirect('/contact')


@login_required(login_url='login')
def userPage(request):

    players = contact.objects.filter(UserProfile = request.user.id)
    return render(request, 'from/user.html', {'players':players})



@login_required(login_url='login')    
def add_travel (request):
    form = add_travelform()
    if request.method == 'POST':
        form = add_travelform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('from/travel.html')
            
    context = {'form':form}
    return render(request, 'from/add_travel.html', context)

@login_required(login_url='login')
def add_music (request):
    form = add_musicform()
    if request.method == 'POST':
        form = add_musicform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('from/music.html')
            
    context = {'form':form}
    return render(request, 'from/add_music.html', context)
    
@login_required(login_url='login')
def add_pass (request):
    form = add_passform()
    if request.method == 'POST':
        form = add_passform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('from/passport.html')
            
    context = {'form':form}
    return render(request, 'from/add_pass.html', context)

@login_required(login_url='login')
def add_anthem (request):
    form = add_anthemform()
    if request.method == 'POST':
        form = add_anthemform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('from/national_anthem.html')
            
    context = {'form':form}
    return render(request, 'from/add_anthem.html', context)    
    