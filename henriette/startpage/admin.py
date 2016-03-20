from django.contrib import admin
from .models import model_home,model_about

class Admin_home(admin.ModelAdmin):
    fieldsets = [
		(None,               {'fields': ['home_headline']}),
        (None,               {'fields': ['home_text']}),
        ('Date information', {'fields': ['home_pub_date']}),
    ]
	
class Admin_about(admin.ModelAdmin):
    fieldsets = [
		(None,               {'fields': ['about_headline']}),
        (None,               {'fields': ['about_text']}),
        ('Date information', {'fields': ['about_pub_date']}),
    ]

admin.site.register(model_home, Admin_home)
admin.site.register(model_about, Admin_about)