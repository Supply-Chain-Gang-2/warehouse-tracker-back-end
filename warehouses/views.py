from django.contrib.auth.models import AnonymousUser
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import Warehouse
from .permissions import IsOwnerOrReadOnly
from .serializers import WarehouseSerializer
from django.shortcuts import redirect


class WarehouseList(ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    serializer_class = WarehouseSerializer

    queryset = Warehouse.objects.all()

    def get_queryset(self):
        user = self.request.user
        if not isinstance(user, AnonymousUser):
            queryset = Warehouse.objects.filter(owner=user)
            return queryset
        else:
            # return redirect(
            #     reverse('login')
            # )
            queryset = Warehouse.objects.all()
            return queryset


class WarehouseDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    serializer_class = WarehouseSerializer

    @property
    def queryset(self):
        user = self.request.user
        queryset = Warehouse.objects.filter(owner=user)
        return queryset
