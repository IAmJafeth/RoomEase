from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm, LoginForm, AccountForm


# Create your views here.

def loginUser(request, success=None):
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
                args['form'] = form
                return render(request, 'auth/login.html', args)
        else: 
            print(form.errors)
            args['form'] = form
            return render(request, 'auth/login.html', args)
    else:
        form = LoginForm()
        args['form'] = form

        if success:
            args['success'] = True
        return render(request, 'auth/login.html', args)

def signupUser(request):
    args = {}

    if request.method == 'POST':
        user_form = SignupForm(data=request.POST)
        account_form = AccountForm(data=request.POST)
        if user_form.is_valid() and account_form.is_valid():
            print("valid")
            user = user_form.save(commit=False)
            try:
                account_form.save(user=user)
            except Exception as e:
                print(e)
                user.delete()
                account_form.add_error('__all__', 'Error saving account')
                args['user_form'] = user_form
                args['account_form'] = account_form
                return render(request, 'auth/signup.html', args)
            user.save()
            return redirect('login', success='true')

        else:
            args['user_form'] = user_form
            args['account_form'] = account_form
            return render(request, 'auth/signup.html', args)
    else:
        user_form = SignupForm(prefix='user')
        account_form = AccountForm(prefix='account')
        args['user_form'] = user_form
        args['account_form'] = account_form
        return render(request, 'auth/signup.html', args)
