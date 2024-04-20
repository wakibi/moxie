from django.core.exceptions import ValidationError
from rest_framework import serializers

from medspa.models import Appointment, Service


class ServiceSerializer(serializers.ModelSerializer):
    

    class Meta:
        fields = '__all__'
        model = Service
        read_only_fields = ('id',)

class AppointmentSerializer(serializers.ModelSerializer):
    start_time = serializers.DateTimeField()
    type = serializers.CharField()
    
    class Meta:
        fields = ('__all__')
        model = Appointment
        read_only_fields = ('id',)
        