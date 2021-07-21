from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import HStoreField, ArrayField
from django.db import models
from django.db.models.fields.related import ForeignKey
from warehouse_utilities.warehouse_constructor import Shelves
from django.urls import reverse

class Warehouse(models.Model):
    name = models.CharField(max_length=256, default="Big Warehouse")
    owner = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=True, blank=True
    )
    description = models.TextField(default="", null=True, blank=True)

    measurement_unit = models.CharField(
        max_length=20,
        default="inches",
        choices=(("feet", "Feet"), ("inches", "Inches")),
    )
    length = models.PositiveIntegerField(default=600)
    width = models.PositiveIntegerField(default=600)
    height = models.PositiveIntegerField(default=120)
    lane_width_size = models.PositiveIntegerField(default=48)
    shelf_length = models.PositiveIntegerField(default=120)
    shelf_depth = models.PositiveIntegerField(default=48)
    shelf_height = models.PositiveIntegerField(default=60)

    @property
    def area(self):
        return self.length * self.width

    @property
    def volume(self):
        return self.area * self.height

    @property
    def x_grid_space(self):
        return (self.width - self.lane_width_size) // (self.shelf_length)

    @property
    def y_grid_space(self):
        return (self.length - self.shelf_depth - self.lane_width_size) // (
            self.shelf_depth + self.lane_width_size
        )

    @property
    def z_grid_space(self):
        return self.height // self.shelf_height

    @property
    def leftover_x_space(self):
        return self.width - (self.x_grid_space * self.shelf_length)

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse("warehouse_detail_view", args=[str(self.id)])

class Item(models.Model):
    warehouse = models.ForeignKey(
        Warehouse, on_delete=models.CASCADE
    )
    item_name = models.CharField(max_length=256, default="")
    units_in_inventory = models.PositiveIntegerField(default=0)
    units_sold = models.PositiveIntegerField(default=0)
    units_recieved = models.PositiveIntegerField(default=0)