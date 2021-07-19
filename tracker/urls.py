from django.urls import path
from .views import HomePageView, AboutUsPageView, SearchPage


urlpatterns = [
  path('', HomePageView.as_view(), name='home.html'),
  path('about/', AboutUsPageView.as_view(), name='about.html'),
  path('search/', SearchPage.as_view(), name='search.html'),
]
