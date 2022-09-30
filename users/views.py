from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
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
