from django.contrib import admin
from static_texts.models import StaticText

class StaticTextAdmin(admin.ModelAdmin):
    list_editable = ('text',)
    list_display = ('place', 'text')

admin.site.register(StaticText, StaticTextAdmin)
