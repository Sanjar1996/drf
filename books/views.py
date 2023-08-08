from .models import BookModel
from .serializers import BookSerializers
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response

# from drf_yasg.openapi import Response
book_model = BookModel.objects.all()


class BookListApiView(generics.ListAPIView):
    queryset = book_model
    serializer_class = BookSerializers


class BookAPIView(APIView):

    def get(self, request):
        book = BookModel.objects.all()
        print(book)
        serializer_data = BookSerializers(book, many=True).data
        data = {
            'status': f"{len(book)} dona kitob",
            'books': serializer_data,
        }

        return Response(data)


class BookCreate(APIView):

    def post(self, request):
        data = request.data
        serializers = BookSerializers(data=data)

        if serializers.is_valid():
            book1 = serializers.save()
            data = {
                'status': 'OK',
                'books': data
            }
            return Response(data)

        return

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
