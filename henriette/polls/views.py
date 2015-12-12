
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Choice, Question
from startpage.views import vote

def pollsView(request):
    polls_list = Question.objects.all()
    vote_info = vote(request)
    
    context = {
        'polls_list': polls_list ,
        'vote_info': vote_info ,
    }
    return render(request, 'pollspage.html', context=context)
