from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from startpage.models import model_home, model_about
#from polls.models import Choice, Question

# Create your views here.
def home(request):
    home_text = getStartpageText()
    
    context = {"home_text": home_text,
    }
    return render(request, 'home.html', context=context)

def getStartpageText():
    try:
        return model_home.objects.get(pk=1)
    except:
        return model_home.objects.all()
		
def about(request):
	about_text = getAboutText()
	context = {"about_text": about_text,
	}
	return render(request, 'about.html', context=context)
	
def getAboutText():
    try:
        return model_about.objects.get(pk=1)
    except:
        return model_about.objects.all()
    

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