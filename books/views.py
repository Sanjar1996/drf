from rest_framework import status
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

class BookApiView(APIView):
    def get(self, request):
        book = BookModel.objects.all()
        serializers_book = BookSerializers(book, many=True).data
        data = {
            'status': f"{len(book)} ta kitob bor",
            'serializer': serializers_book
        }

        return Response(data)


class BookCreateAPIView(APIView):
    def post(self, request):
        # book = BookModel.objects.get(id=pk)
        data = request.data
        serializers = BookSerializers(data=data)
        if serializers.is_valid():
            serializers.save()
            data = {
                'status': "Books saved",
                'serializer': data
            }

            return Response(data)


class BookUpdateView(APIView):

    def get(self, request, pk):
        try:
            book = BookModel.objects.get(id=pk)
            serializer_data = BookSerializers(book).data

            data = {
                'status': "Updated",
                'serializer': serializer_data
            }
            return Response(data, status=status.HTTP_200_OK)
        except Exception:
            data = {
                'status': 'False',
                'message': 'Bad Request',
            }
            return Response(data, status=status.HTTP_404_NOT_FOUND)


class BookListAPIView(APIView):

    def get(self, request, pk):
        try:
            book = BookModel.objects.get(id=pk)
            serializer = BookSerializers(book).data
            data = {
                'status': status.HTTP_200_OK,
                'serializer': serializer
            }
            return Response(data)
        except Exception:
            data = {
                'status': status.HTTP_400_BAD_REQUEST,
                'message': 'Xatolik mabjud'
            }
            return Response(data)


class BookUpdate(APIView):
    def put(self, request, pk):
        book = BookModel.objects.get(id=pk)
        data = request.data
        serializer = BookSerializers(instance=book, data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            data = {
                'status': status.HTTP_201_CREATED,
                'book': data
            }
            return Response(data)


class BookDeleteView(APIView):
    def delete(self, request, pk):
        try:
            book = BookModel.objects.get(id=pk)
            book.delete()
            data = {
                'status': status.HTTP_200_OK,
                'message': "Kitob o'chirildi"
            }

            return Response(data)
        except Exception:
            data = {
                'status': status.HTTP_404_NOT_FOUND,
                'message': "Kitob topilmadi"
            }
            return Response(data)