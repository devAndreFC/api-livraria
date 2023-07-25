from rest_framework.viewsets import ModelViewSet

from core.models import Purchase
from core.serializers import PurchaseSerializer


class PurchaseViewSet(ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
