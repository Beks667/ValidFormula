from django.urls import path
from .views import FormulaCheckViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('formulas', FormulaCheckViewSet, basename='complaints')

urlpatterns = router.urls
