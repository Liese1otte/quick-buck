from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpResponse, HttpRequest


def user_login(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        username = request.POST["usr"]
        password = request.POST["pwd"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            messages.success(request, ("Login error, retry."))
            return redirect("login")
    else:
        return render(request, "registration/login.html", {})


def user_logout(request: HttpRequest) -> HttpResponse:
    logout(request)
    messages.success(request, "Logged out")
    return redirect("home")


def user_register(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():  # TODO: indent remove
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            print(form)
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registered"))
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(
        request,
        "registration/register.html",
        {
            "form": form,
        },
    )
