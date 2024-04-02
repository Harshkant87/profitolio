from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, CreateRecordForm, UpdateRecordForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import Record
from django.contrib import messages

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

# - Create a record 

@login_required(login_url='my-login')
def create_record(request):

    form = CreateRecordForm()

    if request.method == "POST":

        form = CreateRecordForm(request.POST)

        if form.is_valid():
            cp = form.cleaned_data['buy_price']
            sp = form.cleaned_data['sell_price']
            returns = ((sp - cp) / cp) * 100

            instance = form.save(commit=False)
            instance.returns = returns #calculating returns and saving here
            instance.save()
            
            messages.success(request, "Your record was created!")

            return redirect("dashboard")

    context = {'form': form}

    return render(request, 'profitolio/create-record.html', context=context)

# update a record
@login_required(login_url='my-login')
def update_record(request, pk):
    
    record = Record.objects.get(id = pk)
    form = UpdateRecordForm(instance = record)

    if request.method == "POST":

        form = UpdateRecordForm(request.POST, instance = record)

        if form.is_valid():
            cp = form.cleaned_data['buy_price']
            sp = form.cleaned_data['sell_price']
            returns = ((sp - cp) / cp) * 100

            instance = form.save(commit=False)
            instance.returns = returns #calculating returns and saving here
            instance.save()
            
            messages.success(request, "Your record was created!")

            return redirect("dashboard")

    context = {'form': form}

    return render(request, 'profitolio/update-record.html', context=context)

# - Read / View a singular record

@login_required(login_url='my-login')
def singular_record(request, pk):

    all_records = Record.objects.get(id=pk)

    context = {'record':all_records}

    return render(request, 'profitolio/view-record.html', context=context)

# - Delete a record

@login_required(login_url='my-login')
def delete_record(request, pk):

    record = Record.objects.get(id=pk)

    record.delete()

    messages.success(request, "Your record was deleted!")

    return redirect("dashboard")

#Logout
def user_logout(request):
    auth.logout(request)
    return redirect("my-login")

