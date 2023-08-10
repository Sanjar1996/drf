# from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import BookModel
from .serializers import BookSerializers

book_model = BookModel.objects.all()


#
# class BookListApiView(generics.ListAPIView):
#     queryset = book_model
#     serializer_class = BookSerializers
#
#
# class BookAPIView(APIView):
#
#     def get(self, request):
#         book = BookModel.objects.all()
#         print(book)
#         serializer_data = BookSerializers(book, many=True).data
#         data = {
#             'status': f"{len(book)} dona kitob",
#             'books': serializer_data,
#         }
#
#         return Response(data)
#
#
# class BookCreate(APIView):
#
#     def post(self, request):
#         data = request.data
#         serializers = BookSerializers(data=data)
#
#         if serializers.is_valid():
#             book1 = serializers.save()
#             data = {
#                 'status': 'OK',
#                 'books': data
#             }
#             return Response(data)
#
#         return Response(data)
#
#
# class BookDetail(APIView):
#
#     def get(self, request, pk):
#         book = BookModel.objects.get(id=pk)
#         serializer = BookSerializers(book).data
#
#
# class BookDetailView(generics.RetrieveAPIView):
#     queryset = book_model
#     serializer_class = BookSerializers
#
#
# class BookDeleteView(generics.DestroyAPIView):
#     queryset = book_model
#     serializer_class = BookSerializers
#
#
# class BookUpdateView(generics.UpdateAPIView):
#     queryset = book_model
#     serializer_class = BookSerializers
#
#
# class BookCreateView(generics.CreateAPIView):
#     queryset = book_model
#     serializer_class = BookSerializers
#
#
# class Book(generics.ListCreateAPIView):
#     queryset = book_model
#     serializer_class = BookSerializers
#
#
# class BookDeleteUpdateView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = book_model
#     serializer_class = BookSerializers
#
#
# class BookApiView(APIView):
#
#     def get(self, request):
#         book = BookModel.objects.all()

class BookListApiView(APIView):
    def get(self, request):
        book = BookModel.objects.all()
        serializers_book = BookSerializers(book, many=True).data
        data = {
            'status': f"{len(book)} ta kitob bor",
            'serializer': serializers_book
        }

        return Response(data)


class BookDetailAPIView(APIView):
    def post(self, request, pk):
        book = BookModel.objects.get(id=pk)

        serializers = BookSerializers(book).data
