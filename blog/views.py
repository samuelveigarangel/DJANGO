# Create your views here. Criar views por funções
from django.views.generic import DetailView, ListView
from .models import Post
from django.shortcuts import render


def PostListView(request):
    context = {"post_list": Post.objects.all()}
    return render(request, 'blog/post_list.html', context)


def PostDetailView(request, slug):
    context = {"detail_list": Post.objects.get(slug=slug)}
    return render(request, 'blog/post_detail.html', context)


#view class
'''
class PostListView(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post
'''
