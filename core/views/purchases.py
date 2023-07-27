from rest_framework.viewsets import ModelViewSet

from core.models import Purchase
from core.serializers import PurchaseSerializer, CreateEditPurchase


class PurchaseViewSet(ModelViewSet):
    queryset = Purchase.objects.all()
    # serializer_class = PurchaseSerializer

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return PurchaseSerializer
        return CreateEditPurchase

    def get_queryset(self):
        user = self.request.user
        if user.groups.filter(name='Administradores'):
            return Purchase.objects.all()

        return Purchase.objects.filter(user=user)
