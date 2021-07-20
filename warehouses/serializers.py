from rest_framework import serializers
from .models import Warehouse


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = (
            'name', 
            'owner', 
            'description', 
            'length', 
            'width', 
            'height', 
            'lane_width_size', 
            'shelf_length', 
            'shelf_depth', 
            'shelf_height',
            'area',
            'volume',
            'x_grid_space',
            'y_grid_space',
            'z_grid_space',
            'leftover_x_space',
            )
