from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, CreateView
from .models import Post


# Create your views here.
class TopicListView(ListView):
    model = Post
    template_name = "home.html"

class TopicDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"

class TopicCreateView(CreateView):
    model = Post
    template_name = "post_new.html"
    fields = "__all__"

class TopicUpdateView(UpdateView):
    model = Post
    template_name = "post_edit.html"
    fields = ["title", "body"]