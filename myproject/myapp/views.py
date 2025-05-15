from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse
import requests
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
import openai
from .models import Food

def generate_description(food_name):
    # Example implementation of the function
    return f"The food '{food_name}' is delicious and nutritious."


openai.api_key = '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'



def base(request):
    return render(request,'base.html')

def index(request):
    if request.method == 'POST':
        food_name = request.POST.get('food_name', '').strip()
        if food_name:
            description = generate_description(food_name)
            return render(request, 'index.html', {'description': description})
        else:
            messages.error(request, "Please enter a food name.")
            return redirect('index')
    else:
        # Handle GET request or other logic here
        pass
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
    query = request.GET.get("query", "").strip().lower()
    print(f"Search query: {query}")  # Debugging: Log the query
    if not query:
        return JsonResponse({"error": "No query provided."}, status=400)

    results = Food.objects.filter(name__icontains=query)

    foods = []
    for food in results:
        foods.append({
            "id": food.id,
            "name": food.name,
            "image": food.image.url,
            "importance": food.importance,
        })

    return JsonResponse({"foods": foods})