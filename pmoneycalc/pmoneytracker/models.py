from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Payment(models.Model):
    """Model definition for Payment."""
    child = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="payment", null=False)
    parent = models.CharField(max_length=150)
    payment = models.FloatField()
    created = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Payment."""

        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'
