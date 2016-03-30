from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from startpage.models import model_home, model_about
from polls.models import Question, Choice
from .forms import about_headline_form
from django.forms import ModelForm
from django.utils import timezone
import datetime

#from polls.models import Choice, Question

# Create your views here.
def home(request):
	vote_info = vote(request)
	#if request.method == 'POST':
		#a = Choice.objects.get(pk=pk)
		#f = polls_form(request.POST)
	#	a = Choice.objects.all()[0]
	#	a.votes += 1
	#	return HttpResponseRedirect('/about/')
		
	home_text = model_home.objects.all()
	#vote_question = Question.objects.all()[0]#.ordered_by('-pk')[0]
	#vote_choices = Choice.objects.all()
	context = {
		'home_text': home_text,
		'vote_info': vote_info
		#'vote_question': vote_question,
		#'vote_choices': vote_choices,
	}
	return render(request, 'home.html', context=context)

		
def about(request):
	if request.method == 'POST':
		form = about_headline_form()
		return HttpResponseRedirect('/about/')
	else:
		form = about_headline_form()
		about_text = model_about.objects.all()
		context = {
			'about_text': about_text,
			'form': form,
		}
		return render(request, 'about.html', context=context)
	
def edit(request,pk):
		a = model_about.objects.get(pk = pk)
		a.about_pub_date = datetime.datetime.now()
		a.save()
		f = about_headline_form(request.POST, instance=a)
		if f.is_valid():
			f.save()
			return HttpResponseRedirect('/about/')
		form = about_headline_form()
		about_text = model_about.objects.get(pk=pk)
		context = {
			'about_text': about_text,
			'form': form,
			'pk': pk,
		}
		return render(request, 'about_edit.html', context=context)
		
def add(request):
	if request.method == 'POST':
		a = model_about()
		a.about_pub_date = datetime.datetime.now()
		f = about_headline_form(request.POST, instance=a)
		if f.is_valid():
			f.save()
			return HttpResponseRedirect('/about/')
		
	form = about_headline_form(request.POST)
	about_text = model_about.create_object
	about_text.about_pub_date = datetime.datetime.now()
	about_text.about_headline = 'Error1'
	about_text.about_text = 'Error2'
	context = {
		'about_text': about_text,
		}
	return render(request, 'about_add.html', context=context)
	
def delete(request,pk):
	a = model_about.objects.get(pk=pk)
	a.delete()
	return HttpResponseRedirect('/about/')
	

def vote(request):
	question_id = Question.objects.latest('pk').pk
	p = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = p.choice_set.get(pk=request.POST['choice'])
		selected_choice.votes += 1
		selected_choice.save()
	except (KeyError, Choice.DoesNotExist):
		# Redisplay the question voting form.
		return {
				'question': p,
				#'error_message': "You didn't select a choice.",
				'voted': 0,
		} #, 0
	else:
		if request.method == 'POST':
			#HttpResponseRedirect('/home/',)
			return {
					'question': p, 
					'voted' : 1,
			} #, 0
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        #return HttpResponseRedirect(reverse( "/" ,args=1)))
	return {
				'question': p,
				'voted': 1,
	}

		
class about_headline_form(ModelForm):
	class Meta:
		model = model_about
		fields = ['about_headline','about_text']
		
class polls_form(ModelForm):
	class Meta:
		model = Choice
		fields = ['votes']
		