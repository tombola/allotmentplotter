from statistics import mode
from django.db import models


class Plant(models.Model):
    common_name = models.CharField(max_length=255)

    sow_indoors = models.DecimalField()
    transplant = models.DecimalField()
    sow_outdoors = models.DecimalField()
    harvest = models.DecimalField()
