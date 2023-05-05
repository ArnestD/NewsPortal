from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.views.generic import ListView, DetailView
# from django.views.generic.edit import FormView
from  django.views.generic.base import View
from django.core.paginator import Paginator
from .models import *

bad_names = ['incidents', 'Дурак', 'Гад']


class AuthorsPage(ListView):
    model = Author  # queryset = Author.objects.all()
    context_object_name = "Authors"
    template_name = 'news/authors.html'


class PostDetail(View):
    def get(self, request, pk):
        ps = Post.objects.get(id=pk)
        return render(request, "news/posts.html", {'ps':ps})


def news_page_list(request):
    """ Представление для вывода страницы с новостями по заданию """

    newslist = Post.objects.all().order_by('-rating')[:10]
    p = Paginator(newslist, 1)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(10)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
    context = {'page_obj': page_obj}
    return render(request, 'news/news.html', {'newslist': newslist})#context



class search(View):
    search = 'news/search.html'


# class Myform(FormView):
#     form_class = myform
#     success_url = "/succsess/"
#
#     def form_valid(self, form):
#         return super().form_valid(form)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
