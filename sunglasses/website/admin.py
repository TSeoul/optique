
from django.contrib import admin

from .models import Lunettes

class LunettesAdmin(admin.ModelAdmin):

    list_display = ("nom", "description", "en_reduction", "prix", "image")
    search_fields = ["nom"]




admin.site.register(Lunettes, LunettesAdmin)
