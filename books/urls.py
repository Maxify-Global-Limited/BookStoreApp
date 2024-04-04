from django.urls import path
from .views import HomePageView, HomeDetailView, SearchResultsListView


urlpatterns = [
    
    path("", HomePageView.as_view(), name="home"),
    path("book/<int:pk>/", HomeDetailView.as_view(), name="book_detail"),
    path("search/", SearchResultsListView.as_view(),name="search_results"), 
    
]