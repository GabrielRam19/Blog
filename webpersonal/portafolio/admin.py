from pyexpat import model
from django.contrib import admin
from .models import project

# Register your models here.

@admin.register(project)
class ProjectAdmin(admin.ModelAdmin):
    search_fields=('id','title')
    list_display=('id','title','image','descripcion','created')
    readonly_fields=('created','updated')
    list_filter=('created','updated')