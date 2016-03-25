from django import forms
from startpage.models import model_home, model_about
import datetime

class about_headline_form(forms.Form):
	about_headline = forms.CharField(label='about headline', max_length=50)
	about_text = forms.CharField(max_length=1000)
	
#class edit_form(forms.Form):
#	edit_boolean = forms. BooleanField(label='dette blir skrevet på knappen')
	
	#about_pub_date = datetime.datetime.now()
	#about_pub_date = forms.DateTimeField('date published')
	#text = model_home.objects.get(pk=1)
	#text.about_headline = about_headline
	#text.save()
	#def text():
	#	return about_headline
	