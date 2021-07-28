from django.contrib import admin
from django.urls import path, include

from .views import *

app_name = 'articles'

urlpatterns = [
    path('', ArticleListView.as_view(), name = "article-list"),
    path('<int:id>/',ArticleDetailView.as_view(), name = "article-detail"),
    path('<int:id>/delete',ArticleDeleteView.as_view(), name = "article-delete"),
    path('create/', ArticleCreateView.as_view(), name = "article-create"),
    path('<int:id>/update',ArticleUpdateView.as_view(), name = "article-update"),
    ]