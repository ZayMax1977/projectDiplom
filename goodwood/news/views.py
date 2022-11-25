from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from .models import News, Category
from .forms import NewsForm
from django.core.paginator import Paginator

def news(request,page_number=1):
    n = News.objects.all()

    paginator= Paginator(n, 6)
    page_num = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_num)


    categories = Category.objects.all()
    context = {
        "news": n,
        "title": "Список новостей",
        "categories": categories,
        'page_obj': page_obj,

    }
    return render(request, template_name='news/news.html', context=context)



def get_category(request,category_id):
    n = News.objects.filter(category_id=category_id)

    paginator = Paginator(n, 10)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)

    categories = Category.objects.all()
    category = Category.objects.get(id=category_id)
    return render(request, 'news/category.html', { 'news': n,'categories': categories, 'category': category,'page_obj': page_obj})

def view_news(request, news_id):
    news_item = News.objects.get(pk=news_id)
    return render(request,'news/view_news.html', {'news_item': news_item})

def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # return redirect('news')
            return render(request, 'news/add_news_ok.html')
    else:
        form = NewsForm()
        return render(request, 'news/add_news.html',{'form': form})

def add_news_ok(request):
    pass


