from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.PostsView.as_view(), name="PostsView"),
    path("post/<int:pk>", views.DetailedPostView.as_view(), name="DetailedPostView"),
]
