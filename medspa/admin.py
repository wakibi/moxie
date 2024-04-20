from django.contrib import admin

from .models import Appointment, MedSpa, Service

class AppointmentAdmin(admin.ModelAdmin):
    pass

class MedSpaAdmin(admin.ModelAdmin):
    pass

class ServiceAdmin(admin.ModelAdmin):
    pass

# Register your models here.
admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(MedSpa, MedSpaAdmin)
admin.site.register(Service, ServiceAdmin)