from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from startpage.models import Startpage
from polls.models import Choice, Question

# Create your views here.
def StartpageView(request):
    #p = get_object_or_404(Question, pk=question_id)

    # Startpage text burde være funksjon
    startpage_text = getStartpageText()
    
    vote_info = vote(request)
    
    context = {"startpage_text": startpage_text,
        "vote_info": vote_info,
    }
    #try:
    #    return httpRR
    #except:
    return render(request, 'startpage.html', context=context)

def getStartpageText():
    try:
        return Startpage.objects.get(pk=1)
    except:
        return Startpage.objects.all()
    
def vote(request):
    question_id = len(Question.objects.all())
    p = get_object_or_404(Question, pk=question_id)
    

    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
        selected_choice.votes += 1
        selected_choice.save()
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return {
            'question': p,
            'error_message': "You didn't select a choice.",
            'voted': 0,
        } #, 0
    else:
        if request.method == 'POST':

            return {
                'question': p, 
                'voted' : 0,
            } #, 0
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        #return HttpResponseRedirect(reverse( "/" ,args=1,)))
        return {
            'question': p,
            'voted': 1,
        } #, HttpResponseRedirect(reverse( 'startpage' ,args=(1,)))
    
# def vote(request, question_id):
    
    # try:
        # selected_choice = p.choice_set.get(pk=request.POST['choice'])
    # except (KeyError, Choice.DoesNotExist):
        # # Redisplay the question voting form.
        # return render(request, "startpage.html", 
   
        # # Always return an HttpResponseRedirect after successfully dealing
        # # with POST data. This prevents data from being posted twice if a
        # # user hits the Back button.
        # return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))