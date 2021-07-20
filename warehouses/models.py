from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import HStoreField, ArrayField
from django.db import models
from warehouse_utilities.warehouse_constructor import Shelves


class Warehouse(models.Model):
    name = models.CharField(max_length=256,default='Big Warehouse')
    owner = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=True, blank=True
    )
    description = models.TextField(default="", null=True, blank=True)

    measurement_unit = models.CharField(max_length=20, default='inches', choices=(('feet', 'Feet'), ('inches', 'Inches')))
    length = models.IntegerField(default=600)
    width = models.IntegerField(default=600)
    height = models.IntegerField(default=120)
    lane_width_size = models.IntegerField(default=48)
    shelf_length = models.IntegerField(default=120)
    shelf_depth = models.IntegerField(default=48)
    shelf_height = models.IntegerField(default=60)

    @property
    def area(self):
        return self.length * self.width

    @property
    def volume(self):
        return self.area * self.height

    @property
    def x_grid_space(self):
        return (self.width - self.lane_width_size)//(self.shelf_length)

    @property
    def y_grid_space(self):
        return (self.length - self.shelf_depth - self.lane_width_size)//(self.shelf_depth + self.lane_width_size)

    @property
    def z_grid_space(self):
        return (self.height//self.shelf_height)

    @property
    def leftover_x_space(self):
        return self.width-(self.x_grid_space * self.shelf_length)



    # @property
    # def shelves(self):
    #     num_shelves_back_wall = (self.width//self.shelf_length)*(self.height//self.shelf_height)
    #     return x_shelves,y_shelves,z_shelves,num_shelves_back_wall

    # grid = ArrayField(
    #             ArrayField(
    #                 ArrayField(
    #                     models.CharField(max_length=256,default=''),
    #                 ),
    #             ),
    #             default=list,
    # )



    def __str__(self):
        return self.name

    # class TestModel(models.Model):
    # x = models.CharField(max_length=16)
    # z = models.CharField(max_length=16)
    # computed = models.CharField(max_length=32, editable=False)

    # def save(self, *args, **kwargs):
    #     self.computed = self.x + self.y
    #     super(TestModel, self).save(*args, **kwargs)





