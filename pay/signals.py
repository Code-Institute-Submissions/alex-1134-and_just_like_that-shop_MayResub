from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem

#Update order total on line item
@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):

    instance.order.new_total()

# Update order total on line item delete
@receiver(post_delete, sender=OrderLineItem)
def update_on_save(sender, instance, **kwargs):

    instance.order.delete_total()