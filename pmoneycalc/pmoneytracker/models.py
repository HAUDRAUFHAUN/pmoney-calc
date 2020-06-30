from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Payment(models.Model):
    """Model definition for Payment."""
    payment = models.FloatField()
    created = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Payment."""

        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'

    def __str__(self):
        """Unicode representation of Payment."""
        pass
