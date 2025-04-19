from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView

urlpatterns = [
    #path('fbv-index', views.indexView, name='fbv-index'),
    #path('cvb-index', TemplateView.as_view(template_name='index.html'),extra_content={"name":"ali"})
    path('cbv-index', views.IndexView.as_view(),name='cbv-index'),
    path('post/',views.PostList.as_view(),name="post-list")
    
    path('go-to-maktabkhooneh/', RedirectView.as_view(url='https://maktabkhooneh.com/'), name='redirect-to-maktabkhooneh'),
]