from django.urls import include, path

urlpatterns = [
    path('api/medspa/', include('api.medspa.urls', namespace='api-medspa')),
]