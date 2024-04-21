from django.urls import path

from . import views

app_name = 'store'

service_list = views.ServiceViewSet.as_view({'get': 'list', 'post': 'create'})
service_detail = views.ServiceViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update'})
service_medspa_list = views.ServiceViewSet.as_view({'get': 'list_for_medspa'})
appointment_list = views.AppointmentViewSet.as_view({'get': 'list', 'post': 'create'})
appointment_detail = views.AppointmentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update'})
appointment_list_by_status = views.AppointmentViewSet.as_view({'get': 'list_by_status'})
appointment_list_by_start_date = views.AppointmentViewSet.as_view({'get': 'list_by_start_date'})

urlpatterns = [
    path('services/', service_list, name='service-list'),
    path('services/<int:pk>/', service_detail, name='service-detail'),
    path('services/medspa/<int:pk>/', service_detail, name='service-medspa-detail'),
    path('appointments/', appointment_list, name='appointment-list'),
    path('appointments/<int:pk>/', appointment_detail, name='appointment-detail'),
    path('appointments/status/<str:status>/', appointment_list_by_status, name='appointment-detail-status'),
    path('appointments/date/<str:start>/', appointment_list_by_start_date, name='appointment-detail-date'),
]