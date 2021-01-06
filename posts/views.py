from django.shortcuts import render
from django.views.generic import ListView #new
from .models import Post #new --> we're explicitly defining which model we're using.

# Create your views here.
class HomePageView(ListView): #we subclass ListView
	model = Post
	template_name = 'home.html'
	context_object_name = 'all_posts_list' #new
