from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import PostModel


class PostsView(ListView):
    model = PostModel
    template_name = "view_posts.html"


class DetailedPostView(DetailView):
    model = PostModel
    template_name = "detailed_post_view.html"