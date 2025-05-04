from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse
import requests
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User


def base(request):
    return render(request,'base.html')

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()
        print(request.POST)
        if not username or not email or not password:
            messages.error(request, "All fields are required.")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('register')

        user = User.objects.create_user(username=username, password=password)
        user.email = email
        user.save()
        messages.success(request, "Registered successfully.")
        return redirect('login')
    return render(request, 'register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  
        else:
            messages.error(request, "Invalid credentials.")
            return redirect('login')
    return render(request, 'login.html')


def search_food(request):
    query = request.GET.get('query', '')
    if not query:
        return JsonResponse({'error': 'No query provided'}, status=400)

    url = "https://api.edamam.com/api/recipes/v2"
    params = {
        'type': 'public',
        'q': query,
        'app_id': '53938627',
        'app_key': '0e18bd84353f5704d35a0079a2eb3fc4'
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        return JsonResponse(data, safe=False)
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)
