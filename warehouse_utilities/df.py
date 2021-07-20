import pandas as pd

class DataAnalytics:
  """this class takes a dataframe as an argument upon instantiation, and if there is not one, it goes to the given path to create one from a csv.
  """
  def __init__(self, df = None):
      if df is None:
        # we could pass in a path variable here
        self.df = pd.read_csv('warehouse_organization_tool/notebooks/historical.csv')
      else:
        self.df = df

  def get_stats(self):
    """this method gets the standard of deviation, the mean, and the max of each item in terms of sales, inventory numbers, and turnover.
    Returns:
        [2d dictionary]: each dictionary has as a key the name of the item, and as a value another dictionary where the keys are the
        names of statistics, and the values are the number associated with that statistic.
    """
    sales_data = self.df.groupby(self.df["item"]).sales.agg(["std","mean","max"]).to_dict()
    inv_data = self.df.groupby(self.df["item"]).inventory.agg(["std","mean","max"]).to_dict()
    turnover_data = self.df.groupby(self.df["item"]).turnover.agg(["std","mean","max"]).to_dict()
    
    mean = sales_data['mean']
    items = list(mean.keys())

    item_sales_data = {item: {stat: sales_data[stat][item] for stat in sales_data  } for item in items}
    item_inv_data = {item: {stat: inv_data[stat][item] for stat in inv_data  } for item in items}
    item_turnover_data = {item: {stat: turnover_data[stat][item] for stat in turnover_data  } for item in items}
    
    return (item_sales_data, item_inv_data, item_turnover_data)
  
  def get_sorted_max(self):
    """this method returns a dictionary of inventory items sorted with the highest turnover first.
    Returns:
        [dictionary]: all inventory items are sorted from highest turnover to lowest turnover.
    """
    return self.df["turnover"].groupby(self.df['item']).max().sort_values(ascending=False).to_dict()