from django.contrib.auth import get_user_model
from django.db import models


class Warehouse(models.Model):
    name = models.CharField(max_length=256)
    owner = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=True, blank=True
    )
    description = models.TextField(default="", null=True, blank=True)
    # length = ;
    # width = ;
    # height = ;
    # area = ;
    # volume = ;
    # lane_width_size = ;
    # shelves  = ;# <-----------------------gotta figure this out
    # x_grid_space = ;
    # y_grid_space = ;
    # z_grid_space = ;
    # leftover_x_space = ;
    # grid = ; # <--------------------------gotta figure this out
    

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