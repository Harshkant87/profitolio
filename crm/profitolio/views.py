from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm

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
            # return redirect('')

    context = {'form': form}
    return render(request, 'profitolio/register.html', context = context)