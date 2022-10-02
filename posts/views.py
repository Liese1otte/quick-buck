from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import PostModel


class PostsView(ListView):
    model = PostModel
    template_name = "view_posts.html"


class DetailedPostView(DetailView):
    model = PostModel
    context_object_name = "post"
    template_name = "detailed_post_view.html"


class AddPostView(CreateView):
    model = PostModel
    template_name = "add_post_view.html"
    fields = "__all__"
