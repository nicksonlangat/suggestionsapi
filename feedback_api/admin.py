from django.contrib import admin
from .models import Feedback

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('title', 'feedback_type', 'created_at', 'is_resolved')
    list_filter = ('feedback_type', 'is_resolved', 'created_at')
    search_fields = ('title', 'content')
    readonly_fields = ('created_at', 'updated_at')