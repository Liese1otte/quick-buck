from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import PostModel
from django.urls import reverse_lazy


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


class EditPostView(UpdateView):
    model = PostModel
    template_name = "edit_post_view.html"
    fields = "__all__"


class DeletePostView(DeleteView):
    model = PostModel
    context_object_name = "post"
    template_name = "delete_post_view.html"
    success_url = reverse_lazy("PostsView")
