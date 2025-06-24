from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'bankrecon', views.BankReconViewSet)

urlpatterns = [
    path('', include(router.urls)),
]