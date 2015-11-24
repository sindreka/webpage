from django.db import models

import datetime

# Create your models here.
class Startpage(models.Model):
    def __str__(self):
        return self.startpage_text
    pub_date = models.DateTimeField('date published')
    startpage_text = models.TextField(max_length=1000)