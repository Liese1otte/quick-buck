from django.urls import path, include
from . import views


urlpatterns = [
    path("user_login/", views.user_login, name="login"),
    path("user_logout/", views.user_logout, name="logout"),
]
