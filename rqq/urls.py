from django.urls import path
from .views import trigger_event_view

urlpatterns = [
    path('trigger/', trigger_event_view, name='trigger-event'),
]
