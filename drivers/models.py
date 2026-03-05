from django.db import models
from django.contrib.auth.models import User


class DriverProfile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="driver_profile"
    )

    license_number = models.CharField(max_length=100)

    is_available = models.BooleanField(default=False)

    kyc_status = models.CharField(max_length=50)

    rating = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username