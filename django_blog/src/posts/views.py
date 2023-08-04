from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from posts.models import BlogPost

class BlogHome(ListView):
    model = BlogPost
    context_object_name = "posts"

    def get_queryset(self):
        querySet = super().get_queryset()
        if self.request.user.is_authenticated:
            return querySet

        return querySet.filter(published_on=True)

class BlogPostCreate(CreateView):
    model = BlogPost
    template_name = "posts/BlogPost_create.html"
    fields = ["title", "content",]

class BlogPostUpdate(UpdateView):
    model = BlogPost
    template_name = "posts/BlogPost_update.html"
    fields = ["title", "content", "published_on"]
    slug_field = "slug"  

class BlogPostDetail(DetailView):
    model = BlogPost
    context_object_name = "post"

class BlogPostDelete(DeleteView):
    model = BlogPost
    context_object_name = "post"
    success_url = reverse_lazy("posts:home")