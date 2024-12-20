import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def thread_signal_handler(sender, instance, **kwargs):
    print(f"Signal thread ID: {threading.get_ident()}")

def test_signal_thread():
    print(f"Caller thread ID: {threading.get_ident()}")
    User.objects.create(username="threadtestuser")

test_signal_thread()
