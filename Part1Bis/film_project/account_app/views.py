from django.shortcuts import render, redirect
from account_app.forms import SignupForm,LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/film_app/homepage/')

    return render(request, 'signup.html', context={'signup_form': SignupForm()})


def login_auth(request):
  if request.method == 'POST':
    username  = request.POST.get('username')
    password  = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      return redirect('/film_app/homepage/')

  return render(request, 'login.html', context={ 'login_form': LoginForm() })

def logout_auth(request):
  logout(request)
  return redirect('/film_app/')

def profile(request, user_id):
  user = User.objects.get(id=user_id)
  return render(request, 'profile.html', context={ 'user': user })
