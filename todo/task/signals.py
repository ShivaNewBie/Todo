from django.db.models.signals import pre_save 
from django.dispatch import receiver
from django.utils.text import slugify
from django.utils.crypto import get_random_string

from .models import Task

@receiver(pre_save, sender=Task)
def auto_add_slug(sender,instance,*args,**kwargs):
    if instance:
        slug = slugify(instance.description)
        random_string = get_random_string(length=4)
        instance.slug = slug + '-' + random_string