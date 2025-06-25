from django.urls import path, include
from rest_framework import routers
from .bankrecon.views import BankReconViewSet
from .liquidation.views import LiquidationViewSet

router = routers.DefaultRouter()
router.register(r'bankrecon', BankReconViewSet)
router.register(r'liquidation', LiquidationViewSet)

urlpatterns = [
    path('', include(router.urls))
]
