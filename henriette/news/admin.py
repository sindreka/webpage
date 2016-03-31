from django.contrib import admin

# Register your models here.
from .models import model_links

class linksAdmin(admin.ModelAdmin):
    fieldset = [
        #('Date information',{'fields': {'pub_date'}}),
        (None , { 'fields': ['links_title']}),
        (None , { 'fields': ['links_link']}),
        

    ]
    
admin.site.register(model_links,linksAdmin)