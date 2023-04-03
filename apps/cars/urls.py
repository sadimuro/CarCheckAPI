from rest_framework import routers

from apps.cars.views import CarAPIViewSet, SpecialMarksAPIViewSet, PeriodOwnershipAPIViewSet

router = routers.DefaultRouter()
router.register('cars', CarAPIViewSet, "api_cars")
router.register('special', SpecialMarksAPIViewSet, "api_special_marks")
router.register('periods', PeriodOwnershipAPIViewSet, "api_periods_ownership")

urlpatterns = router.urls