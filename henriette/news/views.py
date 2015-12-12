from django.shortcuts import render

# Create your views here.

from .models import News
from startpage.views import vote

def NewsView(request):
    news = News.objects.all()
    vote_info = vote(request)
    context = {
    'news': news ,
    'vote_info': vote_info,
    }
    return render(request, 'newspage.html', context=context)
    
