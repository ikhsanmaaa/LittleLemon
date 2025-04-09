from django.db import models

# Create your models here.
class Booking (models.Model):
    time = [
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        ]
    name = models.CharField(max_length=255)
    reservation_date = models.DateField()
    reservation_time = models.IntegerField(choices = time)