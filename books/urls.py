from django.urls import path

from .views import BookListApiView, BookDetailAPIView

# BookListApiView, BookDetailView, BookUpdateView, BookDeleteView, BookCreateView, \
# BookAPIView, BookCreate


# urlpatterns = [
#     path('', BookListApiView.as_view()),
#     path('<int:pk>/', BookDetailView.as_view()),
#     path('<int:pk>/update/', BookUpdateView.as_view()),
#     path('<int:pk>/delete/', BookDeleteView.as_view()),
#     path('create/', BookCreateView.as_view()),
#     path('apiview/', BookAPIView.as_view()),
#     path('create2/', BookCreate.as_view())
# ]


urlpatterns = [
    path('book/', BookListApiView.as_view()),
    path('book/<int:pk>/', BookDetailAPIView.as_view()),
]
