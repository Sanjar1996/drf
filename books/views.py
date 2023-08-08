from .models import BookModel
from .serializers import BookSerializers
from rest_framework.views import APIView
from rest_framework import generics

book_model = BookModel.objects.all()


class BookListApiView(generics.ListAPIView):
    queryset = book_model
    serializer_class = BookSerializers


class BookDetailView(generics.RetrieveAPIView):
    queryset = book_model
    serializer_class = BookSerializers


class BookDeleteView(generics.DestroyAPIView):
    queryset = book_model
    serializer_class = BookSerializers


class BookUpdateView(generics.UpdateAPIView):
    queryset = book_model
    serializer_class = BookSerializers


class BookCreateView(generics.CreateAPIView):
    queryset = book_model
    serializer_class = BookSerializers


class Book(generics.ListCreateAPIView):
    queryset = book_model
    serializer_class = BookSerializers


class BookDeleteUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = book_model
    serializer_class = BookSerializers


class BookApiView(APIView):

    def get(self, request):
        book = BookModel.objects.all()

