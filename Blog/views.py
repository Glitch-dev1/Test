from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView, ListView
from django.views import View
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import Article
from .forms import *


class ArticleCreateView(CreateView):
    form_class = ArticleModelForm
    template_name = 'Blog/article_create.html'
    queryset = Article.objects.all()
    success_url = '/blog/'

class ArticleDeleteView(DeleteView):
    success_url = '/blog/'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)
    
    queryset = Article.objects.all()

class ArticleListView(View):
    
    def get(self, request, *args, **kwargs):
        template_name = 'Blog/article_list.html'
        queryset = Article.objects.all()
        context = {
        'object_list' : queryset
    }
        return render(request, template_name, context)
 

class ArticleDetailView(DetailView):
    
    queryset = Article.objects.all()
    
    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Article, id = id_)
        
class ArticleUpdateView(UpdateView):
    template_name = 'Blog/article_update.html'
    queryset = Article.objects.all()
    form_class = ArticleModelForm
    success_url = '/blog/'
    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Article, id = id_)