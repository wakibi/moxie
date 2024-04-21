from rest_framework import serializers

from medspa.models import Appointment, Service


class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Service
        read_only_fields = ('id', 'active')
        extra_kwargs = {'medspa': {'required': True}}
        
        
    def validate(self, attrs):
        medspa = attrs.get('medspa', None)
        if not medspa:
            raise serializers.ValidationError('Medspa must be specified')
        request = self.context.get("request")
        if request and not request.user.is_anonymous:
            attrs['added_by'] = request.user
        return super().validate(attrs)


class AppointmentSerializer(serializers.ModelSerializer):
    status = serializers.CharField(required=True)
    class Meta:
        fields = ['id', 'start_time', 'total_duration', 'total_price', 'status', 'medspa', 'services']
        model = Appointment
        read_only_fields = ('id',)
        
    def validate_status(self, value):
        if value == self.instance.status:
            return value
        if value == Appointment.CANCELED and self.instance.status == Appointment.SCHEDULED:
            return value
        if value == Appointment.COMPLETED and self.instance.status == Appointment.SCHEDULED:
            return value
        if self.instance.status == Appointment.CANCELED and value != Appointment.CANCELED:
             raise serializers.ValidationError('You can not update from canceled to another status')
        return value
        
    def validate(self, attrs):
        services = attrs.get('services', None)
        if not services:
            raise serializers.ValidationError('At least one service must be specified')
        medspa = attrs.get('medspa', None)
        for service in services:
            if service.medspa_id != medspa.id:
                raise serializers.ValidationError('One of the services does not belong to provided medspa')
        request = self.context.get("request")
        if request and not request.user.is_anonymous:
            attrs['added_by'] = request.user
        return super().validate(attrs)
