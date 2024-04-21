from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class BaseEntity(models.Model):
    """An abstract model which allows all other models to inherit its characteristics.
    Gives every other model a field for the date it was created and the date it was updated."""
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True, blank=True, null=True)
    added_by = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        abstract = True
        

class MedSpa(BaseEntity):
    name = models.CharField(verbose_name='Name', max_length=255)
    address = models.TextField()
    phone_number = models.CharField(verbose_name='Phone Number', max_length=20)
    email_address = models.EmailField(verbose_name='Email Address')
    active = models.BooleanField()
    
    def __str__(self):
        return f'MedSpa: {self.name}'
    
    
class Service(BaseEntity):
    name = models.CharField(verbose_name='Name', max_length=255)
    description = models.CharField(verbose_name='Description', max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    duration = models.PositiveSmallIntegerField()
    medspa = models.ForeignKey(MedSpa, related_name='services', related_query_name='service', on_delete=models.CASCADE)
    active = models.BooleanField()
    
    class Meta:
        unique_together = (
            ('medspa', 'name')
        )
    
    def __str__(self):
        return f'Service: {self.name}'
    

class Appointment(BaseEntity):
    SCHEDULED = 'SCH'
    COMPLETED = 'COM'
    CANCELED = 'CAN'
    STATUSES = [
        (SCHEDULED, 'Scheduled'),
        (COMPLETED, 'Completed'),
        (CANCELED, 'Canceled'),
    ]
    start_time = models.DateTimeField()
    total_duration = models.PositiveIntegerField(blank=True, null=True)
    total_price = models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=10)
    status = models.CharField(max_length=5, choices=STATUSES, default=SCHEDULED)
    medspa = models.ForeignKey(MedSpa, related_name='appointments', related_query_name='appointment', on_delete=models.CASCADE)
    services = models.ManyToManyField(Service, blank=True, related_name='services', related_query_name='service')
    
    def __str__(self):
        return f'Appointment: {self.id}'
    
