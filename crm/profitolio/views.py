from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import Record

# Create your views here.

# HomePage
def home(request):
    return render(request, 'profitolio/index.html')


# Reister
def register(request):

    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('my-login')

    context = {'form': form}
    return render(request, 'profitolio/register.html', context = context)

#Login a user
def my_login(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request, data = request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username = username, password = password)

            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')
    
    context = {'form2': form}
    return render(request, 'profitolio/my-login.html', context = context)

#dashboard
@login_required(login_url='my-login')
def dashboard(request):

    my_records = Record.objects.all()
    context = {'records': my_records}
    return render(request, 'profitolio/dashboard.html', context = context)


#Logout
def user_logout(request):
    auth.logout(request)
    return redirect("my-login")

