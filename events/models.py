from django.db import models

from free_food_finder.users.models import User


class Event(models.Model):
    TITLE_CHOICES = [
        ("Bhandara", "Bhandara"),
        ("Langarh", "Langarh"),
    ]

    title = models.CharField(
        max_length=100,
        choices=TITLE_CHOICES,
        default="Bhandara"
    )
    description = models.TextField()
    location = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    image = models.ImageField(upload_to="event_images/", blank=True, null=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="events",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-date", "-start_time"]

    def __str__(self):
        return f"{self.title} at {self.location} on {self.date}"
