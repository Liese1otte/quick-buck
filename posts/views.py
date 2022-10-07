from django.shortcuts import render, redirect
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import PostModel
from django.urls import reverse_lazy
from django.http import HttpRequest, HttpResponse
from .models import PostModel


class PostsView(ListView):
    model = PostModel
    template_name = "view_posts.html"


class DetailedPostView(DetailView):
    model = PostModel
    context_object_name = "post"
    template_name = "detailed_post_view.html"


def invite_view(request: HttpRequest, pk) -> HttpResponse:
    return render(request, "invite_to_post.html", {"pk": pk})


def join_view(request: HttpRequest, pk) -> HttpResponse:
    post = PostModel.objects.get(pk=pk)
    post.students.add(request.user.id)
    print(post.students.all())
    return redirect("/posts")


class AddPostView(CreateView):
    model = PostModel
    template_name = "add_post_view.html"
    fields = "__all__"
    
    def form_valid(self, form):
        return redirect("invite_view", form.save().pk)


class EditPostView(UpdateView):
    model = PostModel
    template_name = "edit_post_view.html"
    fields = "__all__"


class DeletePostView(DeleteView):
    model = PostModel
    context_object_name = "post"
    template_name = "delete_post_view.html"
    success_url = reverse_lazy("PostsView")
