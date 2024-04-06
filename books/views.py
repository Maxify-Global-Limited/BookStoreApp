from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from .models import Book

from bookstore_project.settings import MONNIFY_SECRET_KEY, MONNIFY_API_KEY , FLWPUBK_TEST



# Create your views here.

class HomePageView(ListView):
    model = Book
    context_object_name = "book_list"
    template_name = "book/home.html"
    paginate_by = 2
  
    
class HomeDetailView(LoginRequiredMixin, DetailView):
    model = Book
    template_name= "book/book_detail.html"
   
    
  
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = Book.objects.all()
           
        context.update({
                "book_list": queryset,
                "MONNIFY_SECRET_KEY": MONNIFY_SECRET_KEY,
                "MONNIFY_API_KEY": MONNIFY_API_KEY,
                "FLWPUBK_TEST": FLWPUBK_TEST
                
            })
        return context
    
class SearchResultsListView(ListView):
    model = Book
    context_object_name = "book_list"
    template_name = "book/search_results.html"
   
   
    def get_queryset(self): # new
        query = self.request.GET.get("q")
        
        return Book.objects.filter(title__icontains= query)
   