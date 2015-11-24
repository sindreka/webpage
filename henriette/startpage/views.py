from django.shortcuts import render

from news.models import News

# Create your views here.
def ViewNews(request):
    news_list = News.objects.all()
    context = {"news": news_list}
    return render(request, 'startpage.html', context=context)
