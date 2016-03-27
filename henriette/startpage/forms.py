from django import forms
from startpage.models import model_home, model_about
import datetime

class about_headline_form(forms.Form):
	about_headline = forms.CharField(label='about headline', max_length=50)
	about_text = forms.CharField(max_length=1000)
	