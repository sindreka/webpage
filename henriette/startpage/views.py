from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from startpage.models import model_home, model_about
from .forms import about_headline_form
from django.forms import ModelForm
from django.utils import timezone
import datetime

#from polls.models import Choice, Question

# Create your views here.
def home(request):
    home_text = gethomeText()
    
    context = {"home_text": home_text,
    }
    return render(request, 'home.html', context=context)

def gethomeText():
    try:
        return model_home.objects.get(pk=1)
    except:
        return model_home.objects.all()
		
def about(request):
	if request.method == 'POST':
		return HttpResponseRedirect('/edit/')
	else:
		form = about_headline_form()
		about_text = getAboutText()
		context = {
			'about_text': about_text,
			'form': form,
		}
		return render(request, 'about.html', context=context)
	
def edit(request):
	#if request.method == 'POST':
		#form = about_headline_form(request.POST)
		
		#form_text = about_headline_form.text
		#about_text = getAboutText()
		#about_text.about_pub_date = timezone.now()
		#about_text.about_pub_date = 'asfada'
		#about_text.about_headline = form.save()
		a = model_about.objects.all()[0]
		a.about_pub_date = datetime.datetime.now()
		a.save()
		f = about_headline_form(request.POST, instance=a)
		
		
		if f.is_valid():
			f.save()
			return HttpResponseRedirect('/about/')
	#else:
		
		form = about_headline_form()
		about_text = getAboutText()
		context = {
			'about_text': about_text,
			'form': form,
		}
		return render(request, 'edit.html', context=context)
	
	
def getAboutText():
    try:
        return model_about.objects.get(pk=1)
    except:
        return model_about.objects.all()[0]
		
class about_headline_form(ModelForm):
	class Meta:
		model = model_about
		fields = ['about_headline','about_text']
		
#class edit_form(ModelForm):
#	class Meta:
#		model = model_edit
#		fields = ['edit_boolean']
 #def vote(request, question_id):
    
    # try:
        # selected_choice = p.choice_set.get(pk=request.POST['choice'])
    # except (KeyError, Choice.DoesNotExist):
        # # Redisplay the question voting form.
        # return render(request, "startpage.html", 
   
        # # Always return an HttpResponseRedirect after successfully dealing
        # # with POST data. This prevents data from being posted twice if a
        # # user hits the Back button.
        # return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))