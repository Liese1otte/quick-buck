from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.PostsView.as_view(), name="PostsView"),
    path("post/<int:pk>", views.DetailedPostView.as_view(), name="DetailedPostView"),
    path("add_post/", views.AddPostView.as_view(), name="AddPostView"),
    path("post/<int:pk>/edit", views.EditPostView.as_view(), name="EditPostView"),
    path("post/<int:pk>/delete", views.DeletePostView.as_view(), name="DeletePostView"),
    path("post/<int:pk>/invite", views.invite_view, name="invite_view"),
    path("post/<int:pk>/join", views.join_view, name="join_view"),
]
