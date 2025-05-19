from django.contrib import admin
from .models import FarePrediction

@admin.register(FarePrediction)
class FarePredictionAdmin(admin.ModelAdmin):
    list_display = ('pickup_location', 'dropoff_location', 'fare_inr', 'distance', 'duration', 'weather', 'created_at')
    list_filter = ('created_at', 'weather')
    search_fields = ('pickup_location', 'dropoff_location')
