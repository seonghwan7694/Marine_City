from django.shortcuts import render, redirect
from .models import Container
from .form import ContainerForm

from django.views.generic import ListView, DeleteView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import User
from django.contrib import messages
from .form import MyUserCreationForm


# Create your views here.

def main(request):
    return render(request, 'main.html')


def home(request):
    return render(request, 'app/home.html')


def login_page(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username OR password does not exist')

    context = {'page': page}
    return render(request, 'app/login_register.html', context)


def logout_page(request):
    logout(request)
    return redirect('main')


def register_page(request):
    form = MyUserCreationForm()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')

    return render(request, 'app/login_register.html', {'form': form})


"""
def home(request):
    containers = Container.objects.all()
    context = {'containers': containers}
    return render(request, 'app/main.html', context)

def read_container(request, pk):
    container = Container.objects.get(id=pk)
    context = {'container': container}
    return render(request, 'app/container.html', context)

def create_container(request):
    form = ContainerForm()
    context = {'form': form}
    if request.method == 'POST':
        form = ContainerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'app/container_form.html', context)

def update_container(request, pk):
    container = Container.objects.get(id=pk)
    form = ContainerForm(instance=container)
    if request.method == 'POST':
        form = ContainerForm(request.POST, instance=container)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'app/container_form.html', context)

def delete_container(request, pk):
    container = Container.objects.get(id=pk)
    if request.method == 'POST':
        container.delete()
        return redirect('home')
    return render(request, 'app/container_delete.html', {'obj':container})
"""
