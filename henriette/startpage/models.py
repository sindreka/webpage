from django.db import models

import datetime

# Create your models here.
class model_home(models.Model):
    home_pub_date = models.DateTimeField('date published')
    home_text = models.TextField(max_length=1000)
    home_headline = models.CharField(max_length = 50)
	
class model_about(models.Model):
	def create_object(self, about_headline,about_text):
		about_object = self.object.create(about_headline = about_headline,about_text = about_text,about_pub_date = datetime.datetime.now())
		return about_object
		
	about_headline = models.CharField(max_length = 50)
	about_text = models.TextField(max_length=1000)
	about_pub_date = models.DateTimeField('date published')
	