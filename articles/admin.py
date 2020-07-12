from django.contrib import admin
from .models import all_info

# Register your models here.
class Formadmin(admin.ModelAdmin):
    list_display = ('author','title','email','date')
admin.site.register(all_info,Formadmin)