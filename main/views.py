from django.shortcuts import render, redirect
from django.contrib.auth import login
from main.models import Article
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import ListView, TemplateView, DetailView, UpdateView, CreateView, RedirectView
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from accounts.forms import RegistrationForm
from django.contrib import messages


class Home(RedirectView):
    pattern_name = 'main:article-list'


class ArticleListView(ListView):
    model = Article
    paginate_by = 6

    def get_queryset(self):
        articles = super().get_queryset()
        if self.request.GET.get('sub', None) == 'favorites':
            articles = articles.filter(favorites__id=self.request.user.id)
        return articles


class ArticleDetailView(DetailView):
    model = Article
    is_favorite = bool

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_favorite'] = False

        if self.object.favorites.filter(id=self.request.user.id).exists():
            context['is_favorite'] = True

        return context


@method_decorator(login_required, name='dispatch')
class ArticleUpdateView(UpdateView):
    model = Article
    fields = ['favorites']

    def get_success_url(self):
        return reverse_lazy('main:article-detail', args=[self.object.pk])

    def form_valid(self, form):
        if self.object.favorites.filter(id=self.request.user.id).exists():
            self.object.favorites.remove(self.request.user)
            messages.success(self.request, "The article has been removed successfully")

        else:
            self.object.favorites.add(self.request.user)
            messages.success(self.request, "The article has been added successfully")

        form.cleaned_data['favorites'] = self.object.favorites.all()
        return super().form_valid(form)
