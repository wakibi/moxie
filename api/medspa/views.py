from django.db import transaction
from django.shortcuts import get_object_or_404

from rest_framework import viewsets

from medspa.models import Appointment, Service

from .serializers import AppointmentSerializer, ServiceSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    
    
        


class AppointmentViewSet(viewsets.ModelViewSet):
    
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    