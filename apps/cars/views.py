from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
import django_filters.rest_framework
from apps.cars.models import Car
from apps.cars.serializers import CarSerializer

# Create your views here.
class CarAPIView(ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend] 
    filterset_fields = ['license_plate',]
    
    
class CarCreateAPIView(CreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    
    
class CarUpdateAPIView(UpdateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    
class CarDestroyAPIView(DestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    

    
    
    