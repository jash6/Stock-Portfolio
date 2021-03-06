from django.shortcuts import render,redirect
from django.contrib import messages
from django.views.generic import ListView , DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm,EditForm
from django.urls import reverse_lazy
# Create your views here.
# def home(request):
#     return render(request, 'home.html',{})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']

class ArticleDetailView(DetailView):
    model=Post
    template_name = 'article_details.html'

class AddPostView(CreateView):
    model=Post
    form_class =PostForm
    template_name= 'add_post.html'
    # fields= '__all__'

class UpdatePostView(UpdateView):
    model=Post
    template_name = 'update_post.html'
    form_class =EditForm
    # fields =['title','body']


class DeletePostView(DeleteView):
    model=Post
    template_name='delete_post.html'
    success_url = reverse_lazy('home')

def about(request):
    return render(request, 'about.html',{})