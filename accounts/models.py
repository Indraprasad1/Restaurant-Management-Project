from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    class ROLE_CHOICES(models.TextChoices):
        WAITER = 'W', 'Waiter'
        BILLING = 'B', 'Billing'
        KITCHEN = 'K', 'Kitchen'
        OWNER = 'O', 'Owner'
        
    role = models.CharField(choices=ROLE_CHOICES.choices, max_length=2)