from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import HStoreField, ArrayField
from django.db import models


class Warehouse(models.Model):
    name = models.CharField(max_length=256)
    owner = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=True, blank=True
    )
    description = models.TextField(default="", null=True, blank=True)
    length = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()
    area = models.IntegerField()
    volume = models.IntegerField()
    lane_width_size = models.IntegerField()
    shelves  = HStoreField()
    x_grid_space = models.IntegerField()
    y_grid_space = models.IntegerField()
    z_grid_space = models.IntegerField()
    leftover_x_space = models.IntegerField()
    grid = ArrayField(ArrayField(ArrayField(models.CharField(max_length=256, blank=True))))
    

    def __str__(self):
        return self.name
    
    
    
    
    
# self.length = length*12
# self.width = width*12
# self.height = height*12
# self.area = length*width
# self.volume = self.area*height
# self.lane_width_size = 48
# self.shelves = Shelves()
# self.x_grid_space = 0
# self.y_grid_space = 0
# self.z_grid_space = 0
# self.leftover_x_space = 0
# self.grid = None

# class Shelves:
# """this class holds the information for one individual shelf. the warehouse class assumes all of your shelves are the same size.
# """
# def __init__(self, length=10,depth=4,height=5):
# self.length = length*12
# self.depth = depth*12
# self.height = height*12
# self.footprint = self.length*self.depth