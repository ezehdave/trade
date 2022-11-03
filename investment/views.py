from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import User
from django.contrib import messages
from .form import signUpForm
from . models import Profiles ,Investment
from django.http import JsonResponse
import json







# Create your views here.

def login_register(request):
    page = "login"
    if request.user.is_authenticated:
        return redirect('investment')

    if request.method == "POST":
        username = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "user does not exist")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("investment")
        else:
            messages.error(request, "password does not exist")

    context = {'page': page}
    return render(request, 'login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerpage(request):
    form = signUpForm()
    if request.method == "POST":
       form = signUpForm(request.POST)
       if form.is_valid():
            user = form.save(commit=False)
            user.email= user.email.lower()
            user.save()
            login(request, user)
            return redirect("home")
       else:
           messages.error(request, "an error occured during registration")

    context = {'form':form}
    return render(request,'login_register.html', context)



def index(request):
    username = request.user.username
    investment_plans = Investment.objects.filter(user_name__username=username)
    context = {'investment_plans': investment_plans}
    return render(request, 'index.html',context)

def investment(request):
    username = request.user.username
    investment_plans = Investment.objects.filter(user_name__username=username)
    investment_plan = investment_plans
    context={'investment_plan': investment_plan}

    return render(request, 'investment.html',context)

def deposite(request):
    return render(request, 'deposite.html')

def about(request):
    return render(request, 'about.html')

def profile(request):
    username = request.user.username
    investment_plans = Investment.objects.filter(user_name__username=username)
    investment_plan = investment_plans
    context = {'investment_plan': investment_plan,"username": username}

    return render(request, 'profile.html',context )

def withdraw(request):
    return render(request, 'withdraw.html')

def machine(request, pk):
    username = request.user.username
    investment_plans = Investment.objects.filter(user_name__username=username)
    price = pk

    context ={"price": price, "investment_plans": investment_plans}

    return render(request, 'machine.html',context)

def updateItem(request):
    data = json.loads(request.body)
    price = data['form']['price'],
    username = request.user.username
    investment_plans = Investment.objects.get(user_name__username=username)
    prices = price[0]
    investment_plans.investment_plan = prices
    investment_plans.save()


    return JsonResponse( investment_plans.investment_plan , safe=False)









