from django.contrib import admin

# Register your models here.
from .models import News

class NewsAdmin(admin.ModelAdmin):
    fieldset = [
        ('Date information',{'fields': {'pub_date'}}),
        (None , { 'fields': ['news_text']}),
        (None , { 'fields': ['news_title']}),
        

    ]
    
admin.site.register(News,NewsAdmin)