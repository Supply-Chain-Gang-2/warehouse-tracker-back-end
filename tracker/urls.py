from django.urls import path
from .views import HomePageView, AboutUsPageView, SearchPage


urlpatterns = [
  path('', HomePageView.as_view(), name='home.html')
]


