from django.contrib import admin
from .models import Todo

class Todoadmin(admin.ModelAdmin):
    readonly_fields = ('created',)

admin.site.register(Todo, Todoadmin)
# Register your models here.
