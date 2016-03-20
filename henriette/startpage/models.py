from django.db import models

import datetime

# Create your models here.
class model_home(models.Model):
    #def __str__(self):
    #    return self.startpage_text
    home_pub_date = models.DateTimeField('date published')
    home_text = models.TextField(max_length=1000)
    home_headline = models.CharField(max_length = 50)
	
class model_about(models.Model):
	about_headline = models.CharField(max_length = 50)
	about_text = models.TextField(max_length=1000)
	about_pub_date = models.DateTimeField('date published')