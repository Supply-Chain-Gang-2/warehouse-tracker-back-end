from .warehouse_constructor import WarehouseConstructor
import numpy as np
import matplotlib.pyplot as plt



class Warehouse_Visualization(WarehouseConstructor):
  """Extends the Warehouse class. all methods in this class are for rendering the 3d matplot lib bar graph.
  Args:
      Warehouse (class): Contains warehouse specs and measurements
  """
  def __init__(self,**kwargs):
      super().__init__(**kwargs)
      """allows specified arguments to be passed up to the warehouse class upon instantiation
      """
  def calculate_x_pos(self):
    """calculates all of the x positions for each shelf in the warehouse.
    the scaling factor is just the length of one shelf, and it allows the method to keep track of where it is in the x plane.
    
    Returns:
        array: returns an array of all the x positions for each shelf in the warehouse.
    """
    scaling_factor = self.shelves.length
    xpos = []

    for i in range(self.y_grid_space+1):
      counter = 0
      for j in range(1,self.x_grid_space+1):
        #this is the back wall. in english this reads: if you are at the back wall, and youre in the middle of the wall, put another shelf here.
        if (i == self.y_grid_space) and (j == ((self.x_grid_space // 2)+1)):
          xpos.append(counter)
          counter += scaling_factor
          
        #this reads like: if you are in the middle of the rows, put the other rows all the way over on the other wall.
        #self.width - counter is what specifies this.
        if (j == (self.x_grid_space // 2)+1) and not (i == self.y_grid_space):
          xpos.append((counter+(self.leftover_x_space)))
          counter += scaling_factor+self.leftover_x_space
          continue

        #if you are at the beginning of the wall, put the shelf right here and then incriment the counter by 1 shelf.
        if j == 1:
          xpos.append(0)
          counter += scaling_factor
          continue
        
        # if (i == self.y_grid_space) and (j == ((self.x_grid_space))):
        #   xpos.append(counter+scaling_factor)
        #normally just put shelf where the counter tells you to.
        xpos.append(counter)
        counter += scaling_factor
    
    return xpos
  
  def calculate_y_pos(self):
    """calculates the y positions for each shelf in the warehouse.
      the scaling factor is the depth of one shelf plus the space of the walking lane.
    Returns:
        array: returns all of the y positions of each shelf in the warehouse.
    """
    ypos = []
    counter = 0
    scaling_factor = (self.shelves.depth + self.lane_width_size)

    for _ in range(self.y_grid_space+1):
      for _ in range(self.x_grid_space):
        ypos.append(1+counter)
      counter += scaling_factor
    ypos.append(1+counter-scaling_factor)
    
    return ypos
  
  def calculate_z_pos(self):
    """calculates the total number of z spaces for shelvees in the warehouse.
    Returns:
        int: the total number of available z spaces.
    """
    zpos = (self.x_grid_space*(self.y_grid_space+1)) + 1
    return zpos

  def plot_grid(self):
    """this does all of the calculations to determine the position each shelf in the warehouse, and then it plots the 3d graph
    of the warehouse using matplotlib
    """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection = "3d")

    ax.set_xlabel("Width of room in inches")
    ax.set_ylabel("Length of room in inches") 
    ax.set_zlabel("height of room in inches")
    ax.set_xlim3d(0,self.width)
    ax.set_ylim3d(0,self.length)
    ax.set_zlim3d(0,self.height*3) 

    ypos = self.calculate_y_pos()
    zpos = np.zeros(self.calculate_z_pos())
    xpos = self.calculate_x_pos()

    dx = [self.shelves.length-20]
    dy = [self.shelves.depth]
    dz = [self.shelves.height for _ in range(self.z_grid_space)]

    _zpos = zpos   # the starting zpos for each bar
    
    colors = ''
    for _ in range(self.z_grid_space//2):
      colors+='rb'
      
    colors = list(colors)
    for i in range(self.z_grid_space):
        ax.bar3d(xpos, ypos, _zpos, dx, dy, dz[i], color=colors[i], alpha=0.6)
        _zpos += dz[i]    # add the height of each bar to know where to start the next

    plt.gca().invert_xaxis()