from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from .models import Appointment

@receiver(m2m_changed, sender=Appointment.services.through)
def cart_update_total_when_item_added(sender, instance, action, *args, **kwargs):
    if action == 'post_add':
        total_price = 0
        total_duration = 0
        for service in instance.services.all():
            print(service)
            total_price += service.price
            total_duration += service.duration
        instance.total_duration = total_duration
        instance.total_price = total_price
        instance.save()