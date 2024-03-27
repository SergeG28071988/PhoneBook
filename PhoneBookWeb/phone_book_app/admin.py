from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass


@admin.register(Search)
class SearchAdmin(admin.ModelAdmin):
    pass
