from django.shortcuts import render,HttpResponse
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post
from .forms import PostForm,EditForms
from django.urls import reverse_lazy

# # Create your views here.
# def home(request):
#     return render(request,"home.html",{})

# # def home(request):
# #     return HttpResponse("Hi hello world")


#adding blog post to webpage
class HomeView(ListView):
    model = Post
    template_name="home.html"
    # ordering=["-id"]
    ordering=["date_post"]

# adding abstract

class ArticleDetailView(DetailView):
    model = Post
    template_name = "article_detail.html"
# adding table using form tag

# class AddPostView(CreateView):
#     model = Post
#     template_name = "add_post.html"
#     fields='__all__'

class AddPostView(CreateView):
    model = PostForm
    form_class=PostForm
    template_name = "add_post.html"
    
class UpdatePostView(UpdateView):
    model = Post
    form_class=EditForms
    template_name="update_post.html"

class DeletePostView(DeleteView):
    model=Post
    template_name="delete_post.html"
    success_url =reverse_lazy("home")


