from datetime import datetime

from rest_framework import viewsets
from rest_framework.response import Response

from medspa.models import Appointment, Service

from .serializers import AppointmentSerializer, ServiceSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    
    queryset = Service.objects.all().select_related('medspa')
    serializer_class = ServiceSerializer
    
    def list_for_medspa(self, request, *args, **kwargs):
        medspa = self.kwargs['pk']
        queryset = self.queryset.filter(medspa_id=medspa)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

class AppointmentViewSet(viewsets.ModelViewSet):
    
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    
    def list_by_status(self, request, *args, **kwargs):
        status = self.kwargs.get('status', None)
        queryset = self.queryset.filter(status=status)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
    
    def list_by_start_date(self, request, *args, **kwargs):
        start = self.kwargs.get('start', None)
        print(start)
        date_format = '%Y-%m-%d'
        date = datetime.strptime(start, date_format)
        queryset = self.queryset.filter(start_time__gte=date)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
    