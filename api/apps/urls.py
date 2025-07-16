from django.urls import path, include
from rest_framework import routers
from .bankrecon.views import BankReconViewSet
from .liquidation.views import LiquidationViewSet
from .rci.views import *
from .core.views import *

brs_router = routers.DefaultRouter()
brs_router.register(r'bank-reconciliation', BankReconViewSet)

liquidation_router = routers.DefaultRouter()
liquidation_router.register(r'liquidation', LiquidationViewSet)

rci_router = routers.DefaultRouter()
rci_router.register(r'report-of-check-issued', ReportOfCheckIssuedViewSet)
rci_router.register(r'accounting-entry', AccountingEntryViewSet)
rci_router.register(r'rci-payee',RCIPayeeViewSet)
rci_router.register(r'attachment', AttachmentViewSet)

core_router = routers.DefaultRouter()
core_router.register(r'agency', AgencyViewSet)
core_router.register(r'fund', FundViewSet)
core_router.register(r'office', OfficeViewSet)
core_router.register(r'position', PositionViewSet)
core_router.register(r'employee', EmployeeViewSet)
core_router.register(r'expenditure-code', ExpenditureViewSet)

urlpatterns = [
    path('brs/', include(brs_router.urls)),
    path('liquidation/', include(liquidation_router.urls)),
    path('rci/', include(rci_router.urls)),
    path('core/', include(core_router.urls))
]
