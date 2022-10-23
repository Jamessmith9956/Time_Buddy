from argparse import Action
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import routers, serializers, viewsets, status
#https://auth0.com/docs/quickstart/webapp/django/01-login
#from django.contrib.auth.models import User

from rest_framework import status
from rest_framework import filters
from .models import Event, User
from .serializers import EventSerializer, UserSerializer
# Create your views here.
# based on https://www.geeksforgeeks.org/django-rest-api-crud-with-drf/


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

# class AttendeesViewSet(viewsets.ModelViewSet):
#     def get_queryset(self):
#         queryset = User.objects.all()
#         event = Event.objects.filter(event_pk=self.kwargs['event_id'])
#         return queryset.filter(event_pk=self.kwargs['event_pk']).prefetch_related(Prefetch('event_set', queryset=event))
    
class AttendeesViewSet(viewsets.ViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    
    def list(self, request, event_pk=None):
        event = self.queryset.filter(event_id=event_pk).values_list('attendees')
        attendees = User.objects.filter(pk__in=event)
        serializer = UserSerializer(attendees, many=True)
        return Response(serializer.data)
    
    def retrive(self, request, pk=None, event_pk=None):
        attendees = self.queryset.get(pk=pk, event_id=event_pk)
        serializer = UserSerializer(attendees, many=False)
        return Response(serializer.data)
    

# # for info on decorators see - https://stackoverflow.com/questions/6392739/what-does-the-at-symbol-do-in-python
# # @api_view passes the decorated fuction as an argument in the api_view function
# @api_view(['GET'])
# def api_overview(request): #pass in html request
#     api_urls = {
#         'all_events': '/',
#         #to fill out
#     }

#     return Response(api_urls)

# @api_view(['GET', 'DELETE', 'PUT'])
# def get_delete_update_event(request, pk):
#     try:
#         event = Event.objects.get(pk=pk)
#     except Event.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     # get single event
#     if request.method == 'GET':
#         serializer = EventSerializer(event)
#         return Response(serializer.data)
    
#     # update a single event
#     elif request.method == 'PUT':
#         serializer = EventSerializer(event, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     # delete a single event
#     elif request.method == 'DELETE':
#         event.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET', 'POST'])
# def get_post_events(request):
#     # get all events
#     if request.method == 'GET':
#         #events = Event.objects.all()
#         #serializer = EventSerializer(events, many=True)
#         return Response({})#return Response({})#serializer.data)
#     # insert a new event
#     elif request.method == 'POST':
#         data = {
#             'summary': request.data.get('summary'),
#             'location': request.data.get('location'),
#             'description': request.data.get('description'),
#             'dt_start': request.data.get('dt_start'),
#             'dt_end': request.data.get('dt_end')
#         }
        
#         #validate request using serializer, then save
#         serializer = EventSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

 
#@api_view(['GET','POST'])
#def get_post_attendance(request,pk):
#    try:
#        event = Event.objects.get(pk=pk)
#    except Event.DoesNotExist:
#        return Response(status=status.HTTP_404_NOT_FOUND)
#    
#    # get all invitees
#    if request.method == 'GET':
#        #need to update to get users class
#        attendance = Event_Attendance.objects.all() 
#        serializer = EventAttendanceSerializer(attendance, many=True)
#        return Response(serializer.data)
#    # insert a new event
#    elif request.method == 'POST':
#        data = {
#            'event': event,
#            'attendees': request.data.get('location'),
#        }
#        
#        #validate request using serializer, then save
#        serializer = EventSerializer(data=data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status=status.HTTP_201_CREATED)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)