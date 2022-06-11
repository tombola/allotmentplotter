from pyexpat import model
from django.db import models


class Bed(models.Model):
    width = models.DecimalField(max_digits=5, decimal_places=2)
    length = models.DecimalField(max_digits=5, decimal_places=2)


class BedPlanting(models.Model):
    bed = models.ForeignKey("planner.Bed", on_delete=models.CASCADE)
    plant = models.ForeignKey("plants.Plant", on_delete=models.SET_NULL, null=True)
    planting_date = models.DateField()
    harvest_date = models.DateField()
