from django.shortcuts import render

# Create your views here.
from .models import Events
from rest_framework import permissions, viewsets
from rest_framework import request
from .serializers import EventSerializer
from rest_framework.response import Response
from rest_framework import status


class UserEventsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    # queryset = Events.objects.get(user==request.user)
    # get queryset for a specific user 
    queryset = Events.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        user_id = self.request.user.id
        return Events.objects.filter(user=user_id)
    
class EventsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    # queryset = Events.objects.get(user==request.user)
    # get queryset for a specific user 
    queryset = Events.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]
    #TODO use partial patch only for modifying only attendees 
    def destroy(self, request, *args, **kwargs):
        return Response({"error": "Method Not Allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        attendees = request.data.get('attendees', None)
        user_id = request.data.get('user')[0]
        if request.user.id == user_id:            
            if attendees is not None:
                instance.attendees.set(attendees)
                instance.save()
                return Response({'message': 'Attendees updated successfully'})
            else:
                return Response({'error': 'Attendees field is required'}, status=400)
        else:
            return Response({'error': 'Not Allowed to modify other ateendees'}, status=400)
    
