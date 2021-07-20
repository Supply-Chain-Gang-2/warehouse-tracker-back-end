import numpy as np
import pandas as pd
from .df import DataAnalytics

class WarehouseConstructor:
  """the Warehouse class represents a physical warehouse. it contains the measurements of the warehouse, including dimensions, walking lane space,
  the specs of the shelves, the available grid spaces in which to put shelves. all dimensions are in inches. it stores the grid of the warehouse as a 3d numpy array.
  The data_analyzer is what imports all of the statistics from the csv
  """
  #all dimensions in inches
  def __init__(self, length=50, width=50, height=10,df=None, **kwargs):
    self.length = length*12
    self.width = width*12
    self.height = height*12
    self.area = length*width
    self.volume = self.area*height
    self.lane_width_size = 48
    self.shelves = Shelves()
    self.x_grid_space = 0
    self.y_grid_space = 0
    self.z_grid_space = 0
    self.leftover_x_space = 0
    self.grid = None
    self.locations_of_items = {}
    self.data_analyzer = DataAnalytics(df)

    if 'lane_size' in kwargs:
      self.lane_width_size = kwargs['lane_size']*12

  def calculate_num_of_shelves(self):
    """this method calculates number of shelves available for the warehouse,
    with one walking lane down the middle and the shelves spread equally to the left and the right. the back wall has as many shelves
    as will fit across the entire wall.
    Returns:
        [tuple(ints)]: this functions returns the locations of each shelf as a grid space that includes the dimensions of the
        shelf and a walking lane to access the shelf.
    """
    shelf = Shelves()
    num_shelves_back_wall = (self.width//shelf.length)*(self.height//shelf.height)
    x_shelves = (self.width - self.lane_width_size)//(shelf.length)
    y_shelves = (self.length - shelf.depth - self.lane_width_size)//(shelf.depth + self.lane_width_size)
    # z_shelves = (x_shelves + y_shelves + num_shelves_back_wall)*(self.height//shelf.height)
    z_shelves = (self.height//shelf.height)
    self.x_grid_space,self.y_grid_space,self.z_grid_space,self.leftover_x_space = x_shelves,y_shelves,z_shelves, self.width-(x_shelves*shelf.length)
    return x_shelves,y_shelves,z_shelves,num_shelves_back_wall

  def place_shelves(self):
    self.calculate_num_of_shelves()
    self.grid = np.zeros((self.x_grid_space,self.y_grid_space+1,self.z_grid_space), 'U32')
    
  def place_items(self):
    """this method takes the items in inventory from the data analyzer, and places them in the warehouse from 
    left to right, closest to farthest away (farthest away is the back wall).
    """
    #places items from left to right, front to back, bottom to top in order of highest to lowest item turnover
    max_turnover = self.data_analyzer.get_sorted_max()
    items = max_turnover.keys()
    
    #y starts as the y grid space because in the numpy array, the number of y grid spaces denotes the closest row.
    for item in items:
      x,y,z = 0,self.y_grid_space,0
      while True:
        #check to see if there is n item on the shelf.
        shelf_has_item = self.grid[x][y][z]
        #if there is nothing on the shelf, the if statement will evaluate to True and the item will be placed there.
        if not shelf_has_item:
          self.grid[x][y][z] = item
          print(f'placed {item}')
          self.locations_of_items[item] = (x,y,z)
          break
        
        #first, go from left to right on the closest row.
        if x < self.x_grid_space-1:
          x += 1
          continue
        
        #then, go to the next row and start at the left of it.
        if y > 0:
          x = 0
          y -= 1
          continue
        
        # if the entire first floor is full, then start putting items on the top shelves.
        if z < self.z_grid_space-1:
          x = 0
          y = self.y_grid_space
          z += 1
          continue
        
    print(self.grid)
    

class Shelves:
  """this class holds the information for one individual shelf. the warehouse class assumes all of your shelves are the same size.
  """
  def __init__(self, length=10,depth=4,height=5):
    self.length = length*12
    self.depth = depth*12
    self.height = height*12
    self.footprint = self.length*self.depth