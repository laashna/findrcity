from django.db import models


class City(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=True, default=None)

    temperature_high = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    temperature_low = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    precipitation_days = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    precipitation_inches = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    snowfall_days = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    snowfall_inches = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    sunshine_percent = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    sunshine_hours = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    sunshine_clear_days = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    cloud_days = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    fog_days = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    wind_mph = models.DecimalField(max_digits=5, decimal_places=2, null=True)

    population = models.IntegerField(null=True, default=None)

    total_violent_crimes = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    murder = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    rape = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    robbery = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    assault = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    total_property_crimes = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    burglary = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    larceny_theft = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    motor_vehicle_theft = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    arson = models.DecimalField(max_digits=5, decimal_places=2, null=True)

    walkscore = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    transit_score = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    bike_score = models.DecimalField(max_digits=5, decimal_places=2, null=True)

    state = models.ForeignKey('State', on_delete=models.DO_NOTHING, null=True)


class State(models.Model):
    id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=50, null=True, default=None)

