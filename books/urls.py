from django.urls import path

from .views import BookApiView, BookCreateAPIView, BookUpdateView, BookListAPIView, BookUpdate, BookDeleteView

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
    path('book/', BookApiView.as_view()),
    path('book/create/', BookCreateAPIView.as_view()),
    path('book/<int:pk>/update/', BookUpdateView.as_view()),
    path('book/<int:pk>/', BookListAPIView.as_view()),
    path('book/<int:pk>/creade/', BookUpdate.as_view()),
    path('book/<int:pk>/delete/', BookDeleteView.as_view())
]
