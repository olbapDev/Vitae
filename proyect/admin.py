from django.contrib import admin
from .models import Project

class ProjAdmin(admin.ModelAdmin):
    list_display= ["titulo","lenguaje","link"]
    search_fields=["titulo","lenguaje"]
    list_filter =["lenguaje"]
    list_per_page = 5
    #para hacer un campo editable
    #list_editable = ["titulo"]

# Register your models here.
admin.site.register(Project, ProjAdmin)