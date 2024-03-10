from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages
from .forms import SignUpForm
from django.contrib.auth import logout
from store.models import Customer
from django.http import HttpResponse
# Create your views here.

def login_request(request):
    if request.user.is_authenticated:
        return HttpResponse('You are already logged In') # Add your custom html page here
    if request.method == "POST":
        user = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=user, password=password)
        if user is not None:
            login(request, user)
            messages.info(request, f"You are now logged in as {user}.")
            return redirect("store")
        else:
            form = AuthenticationForm()
            messages.error(request,"Invalid username or password.")
            return render(request=request, template_name="login.html", context={"login_form":form})
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form":form})

def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            userObj = form.save()
            name = form.cleaned_data.get("name")
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            userObj.is_superuser = True
            userObj.is_staff = True
            userObj.save()
            Customer.objects.create(user=userObj, name=username, email=email) 
            messages.success(request, "User created successfully")
            return redirect("store")
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Error in {field}: {error}")
            form = SignUpForm()
    else:
        form = SignUpForm()

    return render(request, "register.html", {"form": form})




def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('store')  # Redirect to main home page
    else:
        return HttpResponse('something went wrong')