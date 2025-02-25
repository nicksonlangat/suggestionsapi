from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Feedback
from .serializers import FeedbackSerializer, FeedbackCreateSerializer
from .permissions import IsAdminUser, AllowAnyForCreateOnly

class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    permission_classes = [AllowAnyForCreateOnly]
    
    def get_serializer_class(self):
        if self.action == 'create':
            return FeedbackCreateSerializer
        return FeedbackSerializer
        
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        # Return a simple response without data for anonymous submissions
        return Response({
            "message": "Feedback submitted successfully. Thank you for your input!"
        }, status=status.HTTP_201_CREATED)