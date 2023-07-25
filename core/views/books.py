from rest_framework.viewsets import ModelViewSet

from core.models import Book
from core.serializers import BookSerializer, BookDetailSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return BookDetailSerializer
        if self.action == 'retrieve':
            return BookDetailSerializer
        return BookSerializer
