from django.views import generic
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutUsPageView(TemplateView):
    template_name = 'about.html'

class SearchPage(TemplateView):
    template_name = 'search.html'

class ToolInfoPageView(TemplateView):
    template_name = 'tool_info.html'

class MyWarehousesView(TemplateView):
    template_name = 'my_warehouses.html'
