from django.urls import include, path
#from rest_framework import routers
from rest_framework_nested import routers
from . import views
from .views import EventViewSet, UserViewSet, AttendeesViewSet, AttendeeDeleteView

router = routers.DefaultRouter()
router.register(r'users',UserViewSet)
router.register(r'events',EventViewSet)

attendance_router = routers.NestedSimpleRouter(router, r'events', lookup='event')
attendance_router.register(r'attendees', AttendeesViewSet, basename='event-attendee')
#attendance_router.register(r'attendees/<:attendeeID:>', AttendeeDeleteView)
# 'basename' is optional. Needed only if the same viewset is registered more than once
# Official DRF docs on this option: http://www.django-rest-framework.org/api-guide/routers/

urlpatterns = [
    path(r'', include(router.urls)),
    path(r'', include(attendance_router.urls)),
    path('events/events/<uuid:event_pk>/attendees/<uuid:pk>',include('rest_framework.urls', namespace='restframework')),
    path('auth/', include('rest_framework.urls', namespace='rest_framework'))
]
