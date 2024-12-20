import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def sync_signal_handler(sender, instance, **kwargs):
    print(f"Signal thread ID: {threading.get_ident()}")  


def test_signal():
    print(f"Caller thread ID: {threading.get_ident()}")  
    user = User.objects.create(username="testuser")

test_signal()
