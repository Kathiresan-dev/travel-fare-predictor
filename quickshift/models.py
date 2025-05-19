from django.db import models

class FarePrediction(models.Model):
    VEHICLE_CHOICES = [
        ('bike', 'Bike'),
        ('auto', 'Auto'),
        ('car', 'Car'),
    ]

    pickup_location = models.CharField(max_length=255)
    dropoff_location = models.CharField(max_length=255)
    pickup_lat = models.FloatField()
    pickup_lon = models.FloatField()
    dropoff_lat = models.FloatField()
    dropoff_lon = models.FloatField()
    distance = models.FloatField()
    duration = models.IntegerField()
    surge_multiplier = models.FloatField()
    weather = models.CharField(max_length=50)
    vehicle_type = models.CharField(max_length=10, choices=VEHICLE_CHOICES)  # 🆕 Added this
    fare_inr = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.pickup_location} ➔ {self.dropoff_location} ({self.vehicle_type.title()} ₹{self.fare_inr})"

