from django.contrib import admin
from .models import Startpage

class StartpageAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['startpage_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]

admin.site.register(Startpage, StartpageAdmin)