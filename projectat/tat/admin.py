from django.contrib import admin               # Geekyshows:- 1:21:00

from .models import Destination
# Register your models here.
@admin.register(Destination)


class DestinationModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','prod_img']