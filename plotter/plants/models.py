"""
Plant types and varieties that can be referenced by beds and rows.
"""

from django.db import models


class Plant(models.Model):
    """Plant
    Represents a plant type, eg courgette or asparagus.

    Details such as planting times can be overwritten by more specific `PlantVariety`.
    """

    common_name = models.CharField(max_length=255)

    sow_indoors = models.DecimalField()
    transplant = models.DecimalField()
    sow_outdoors = models.DecimalField()
    harvest = models.DecimalField()
