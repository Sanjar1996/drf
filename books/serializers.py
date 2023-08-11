from rest_framework import serializers, status
from rest_framework.exceptions import ValidationError

from .models import BookModel


class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = BookModel
        fields = (
            'id',
            'title',
            'subtitle',
            'text',
            'author',
            'isbn',
            'price'
        )

    def validate(self, data):
        title = data.get('title', None)
        author = data.get('author', None)
        if not title.isalpha():
            raise ValidationError(
                {
                    'status': status.HTTP_400_BAD_REQUEST,
                    'messseage': 'Xatolik mavjud'
                }
            )
        if BookModel.objects.filter(title=title, author=author):
            raise ValidationError(
                {
                    'status': False,
                    'message': "BU oldin kiritilgan"
                }
            )

        return data
