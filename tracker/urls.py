from django.urls import path
from .views import HomePageView, AboutUsPageView, SearchPage, ToolInfoPageView, MyWarehousesView


urlpatterns = [
  path('home/', HomePageView.as_view(), name='home'),
  path('about/', AboutUsPageView.as_view(), name='about'),
  path('tool_info/', ToolInfoPageView.as_view(), name='tool_info'),
  path('search/', SearchPage.as_view(), name='search'),
  path('my_warehouses/', MyWarehousesView.as_view(), name='my_warehouses'),
]
