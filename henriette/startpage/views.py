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
	home_text = model_home.objects.all()
	vote_question = Question.objects.all()[0]#.ordered_by('-pk')[0]
	vote_choices = Choice.objects.all()
	context = {
		'home_text': home_text,
		'vote_question': vote_question,
		'vote_choices': vote_choices,
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
	
#def polls():#
#	polls_objects = 

		
class about_headline_form(ModelForm):
	class Meta:
		model = model_about
		fields = ['about_headline','about_text']
		