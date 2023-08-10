from rest_framework import serializers

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
