from rest_framework.viewsets import ModelViewSet

from core.models import Publisher
from core.serializers import PublisherSerializer


class PublisherViewSet(ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
