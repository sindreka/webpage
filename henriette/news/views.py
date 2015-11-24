from django.shortcuts import render

# Create your views here.

from .models import News


class NewsView(news):
    news = News.objects.all()
    context = {
    'news': news 
    }
    return render(request, 'news.html', context=context)
    
