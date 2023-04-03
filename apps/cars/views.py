from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin

from apps.cars.models import Car, SpecialMarks, PeriodsOwnership
from apps.cars.serializers import CarSerializer, SpecialMarksSerializer, PeriodsOwnershipSerializer

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAdminUser, AllowAny


# Create your views here.
class CarAPIViewSet(GenericViewSet,
                    ListModelMixin,
                    RetrieveModelMixin,
                    CreateModelMixin,
                    UpdateModelMixin,
                    DestroyModelMixin):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['licience_plate', ]
    
    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            return (AllowAny(), )
        return (IsAdminUser(), )
    
    
class SpecialMarksAPIViewSet(GenericViewSet,
                            ListModelMixin,
                            RetrieveModelMixin,
                            CreateModelMixin,
                            UpdateModelMixin,
                            DestroyModelMixin):
    queryset = SpecialMarks.objects.all()
    serializer_class = SpecialMarksSerializer
    
    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            return (AllowAny(), )
        return (IsAdminUser(), )
    
    
    
class PeriodOwnershipAPIViewSet(GenericViewSet,
                                ListModelMixin,
                                RetrieveModelMixin,
                                CreateModelMixin,
                                UpdateModelMixin,
                                DestroyModelMixin):
    queryset = PeriodsOwnership.objects.all()
    serializer_class = PeriodsOwnershipSerializer
    
    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            return (AllowAny(), )
        return (IsAdminUser(), )
                                