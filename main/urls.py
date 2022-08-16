from django.urls import path
from . import views
from .views import Home, ArticleListView, ArticleDetailView, ArticleUpdateView

app_name = 'main'

urlpatterns = [
    # Articles
    path('', Home.as_view(), name='home'),
    path('articles', ArticleListView.as_view(), name='article-list'),
    path('articles/<uuid:pk>', ArticleDetailView.as_view(), name="article-detail"),
    path('articles/<uuid:pk>/update',
         ArticleUpdateView.as_view(), name="article-update"),
]
