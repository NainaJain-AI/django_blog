from django.contrib import admin
from .models import JournalEntry

@admin.register(JournalEntry)
class JournalAdmin(admin.ModelAdmin):
    list_display = ('date', 'title', 'user', 'mood')
    list_filter = ('date', 'user')
    search_fields = ('title', 'content')