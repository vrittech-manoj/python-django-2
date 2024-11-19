from django.dispatch import receiver
from django.db.models.signals import pre_save,post_save,pre_delete
from .models import Task

@receiver(post_save, sender=Task)  
def post_save_if_task_is_created(sender, instance, created, **kwargs):
    if created:
        print("*********************")
        print("data is created ",instance)
    
@receiver(pre_delete, sender=Task)  
def delete_if_task_is_delete(sender, instance, **kwargs):
        print("*********************")
        print("data is deleted ",instance)