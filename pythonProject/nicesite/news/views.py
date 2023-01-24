
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import News, Category
from .forms import NewsForm
from django.core.paginator import Paginator

# Create your views here.
def test(request):
    objects = ['dima1', 'vasya2', 'kolya3', 'niwa5', 'vasya6', 'kolya7']
    paginator = Paginator(objects, 2)
    page_num = request.GET.get('page', 1)
    page_objects = paginator.get_page(page_num)
    return render(request, 'news/test.html', {'page_obj': page_objects})


class HomeNews(ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    #extra_context = {'title', 'Главная'}
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True)

class NewsByCategory(ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True)

class ViewNews(DetailView):
    model = News
    #pk_url_kwarg = 'news_id'
    context_object_name = 'news_item'


#def index(request):
    #context = {
        #'news': news,
        #'title': 'Список новостей',
    #return render(request, 'news/index.html', context)

class CreateNews(CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'


#def get_category(request, category_id):
#    news = News.objects.filter(category_id=category_id)
#
#    category = Category.objects.get(pk=category_id)
#    context = {
#        'news': news,
#        'category': category
#    }
#    return render(request, 'news/category.html', context)


#def view_news(request, news_id):
    # news_item = News.objects.get(pk=news_id)
#    news_item = get_object_or_404(News, pk=news_id)
#    context = {
#        'news_item': news_item
#    }
#    return render(request, 'news/view_news.html', context)


#def add_news(request):
    #form = NewsForm(request.POST)
        #if form.is_valid():
            # print(form.cleaned_data)
            #news = News.object.create(**form.cleaned_data)
            #news = form.save()
            #return redirect(news)
    ######return render(request, 'news/add_news.html', context)
