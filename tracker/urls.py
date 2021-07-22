from django.urls import path
from .views import HomePageView, AboutUsPageView, ToolInfoPageView


urlpatterns = [
  path('', HomePageView.as_view(), name='home'),
  path('about/', AboutUsPageView.as_view(), name='about'),
  path('tool_info/', ToolInfoPageView.as_view(), name='tool_info'),
#   path('my_warehouses/', MyWarehousesView.as_view(), name='my_warehouses'),
]
