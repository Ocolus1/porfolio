from django.contrib import admin
from .models import Feedback

class FeedbackAdmin(admin.ModelAdmin): 
    list_display = ("id", "name", "email")
    list_display_links = ("id", "name")

admin.site.register(Feedback, FeedbackAdmin)
