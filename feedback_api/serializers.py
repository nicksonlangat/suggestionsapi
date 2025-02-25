from rest_framework import serializers
from .models import Feedback

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['id', 'feedback_type', 'title', 'content', 'created_at', 'updated_at', 'is_resolved']
        read_only_fields = ['id', 'created_at', 'updated_at']
        
class FeedbackCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['feedback_type', 'title', 'content']