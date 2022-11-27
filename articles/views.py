from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Articles
# Create your views here.


class ArticleListView(ListView):
    model = Articles
    template_name = 'article_list.html'


class ArticleDetailView(DetailView):  # new
    model = Articles
    template_name = 'article_detail.html'


class ArticleUpdateView(UpdateView):  # new
    model = Articles
    fields = ('title', 'body',)
    template_name = 'article_edit.html'


class ArticleDeleteView(DeleteView):  # new
    model = Articles
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
