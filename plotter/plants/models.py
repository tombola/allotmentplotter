"""
Plant types and varieties that can be referenced by beds and rows.
"""

from django.db import models


class Plant(models.Model):
    """
    Represents a plant type, eg courgette or asparagus.

    Details such as planting times can be overwridden by more specific `PlantVariety`.
    """

    common_name = models.CharField(max_length=255)
    latin_name = models.CharField(max_length=255)

    # Month planting guidelines use 1-12
    # numeric options allows ranges
    # decimal places allow early/late month descriptions
    sow_indoors_earliest = models.DecimalField(
        null=True, blank=True, max_digits=4, decimal_places=2
    )
    sow_indoors_latest = models.DecimalField(
        null=True, blank=True, max_digits=4, decimal_places=2
    )
    transplant_earliest = models.DecimalField(
        null=True, blank=True, max_digits=4, decimal_places=2
    )
    transplant_latest = models.DecimalField(
        null=True, blank=True, max_digits=4, decimal_places=2
    )
    sow_outdoors_earliest = models.DecimalField(
        null=True, blank=True, max_digits=4, decimal_places=2
    )
    sow_outdoors_latest = models.DecimalField(
        null=True, blank=True, max_digits=4, decimal_places=2
    )
    harvest_earliest = models.DecimalField(
        null=True, blank=True, max_digits=4, decimal_places=2
    )
    harvest_latest = models.DecimalField(
        null=True, blank=True, max_digits=4, decimal_places=2
    )

    def __str__(self):
        return self.common_name
