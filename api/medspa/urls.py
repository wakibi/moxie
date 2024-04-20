from django.urls import path
from rest_framework import routers

from . import views

app_name = 'store'

router = routers.DefaultRouter()
router.register(r'appointments', views.AppointmentViewSet, 'appointment')
router.register(r'services', views.ServiceViewSet, 'service')

urlpatterns = []

urlpatterns += router.urls