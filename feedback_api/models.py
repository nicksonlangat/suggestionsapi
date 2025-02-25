from django.db import models
import uuid

class Feedback(models.Model):
    SUGGESTION = 'suggestion'
    COMPLAINT = 'complaint'
    GENERAL = 'general'
    
    FEEDBACK_TYPES = [
        (SUGGESTION, 'Suggestion'),
        (COMPLAINT, 'Complaint'),
        (GENERAL, 'General Feedback'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    feedback_type = models.CharField(max_length=20, choices=FEEDBACK_TYPES, default=GENERAL)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_resolved = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.get_feedback_type_display()}: {self.title}"