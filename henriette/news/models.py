from django.db import models


import datetime

class model_links(models.Model):
	links_title = models.CharField(max_length=200)
	links_link = models.CharField(max_length=200)
#    def __str__(self):
#        return self.news_title
#    pub_date = models.DateTimeField('date published')
#    def getTitle(self):
#        return self.news_title
#    def getText(self):
#        return self.news_text
#    news_title = models.CharField(max_length=200)
#    news_text = models.TextField(max_length=1000)
        