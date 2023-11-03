from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm, LoginForm

# Create your views here.

def loginUser(request):
    args = {}
    
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            remember_me = form.cleaned_data['remember_me']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                print("login success")
                if not remember_me:
                    print("not remember me")
                    request.session.set_expiry(0)
                login(request=request, user=user)
                return redirect('home')
            else:
                args['login_error'] = "Username or password is incorrect"
                args['form'] = form
                return render(request, 'auth/login.html', args)
        else: 
            args['login_error'] = "Please enter a correct username and password. Note that both fields are case-sensitive."
            args['form'] = form
            return render(request, 'auth/login.html', args)
    else:
        form = LoginForm()
        args['form'] = form
        return render(request, 'auth/login.html', args)

def signupUser(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'auth/signup.html', {'form': form})
