from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from .models import Post
# Create your views here.


def indexView(request):
    """_summary_
    a function based view to show index page
    """
    return render(request,"index.html")

class IndexView(TemplateView):
    """
    a class based view to show index page
    """
    template_name = 'index.html'
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["name"]="ali"
        context["posts"] = Post.objects.all()
        return context
    
    
    
class PostList(ListView):
    model = Post
    