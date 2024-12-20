from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db import transaction

@receiver(post_save, sender=User)
def transaction_signal_handler(sender, instance, **kwargs):
    transaction.on_commit(lambda: print("Signal after commit"))

def test_signal_transaction():
    print("Creating user...")
    user = User.objects.create(username="transactiontestuser")
    print("User created!")

test_signal_transaction()
