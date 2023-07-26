from rest_framework.exceptions import ValidationError
from .models import Book
from rest_framework import serializers


# class BookSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Book
#         fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate(self, data):
        title = data.get('title', None)
        author = data.get('author', None)
        if not title.isalpha():
            raise serializers.ValidationError({
                'status': False,
                'message': "Please enter a title consisting of letters only"
            })
        if Book.objects.filter(title=title, author=author).exists():
            raise serializers.ValidationError({
                'status': False,
                'message': "Book with the same title and author already exists"
            })
        return data

    def validate_price(self, price):
        if price < 0 or price > 999999999:
            raise serializers.ValidationError({
                'status': False,
                'message': "Price is out of range"
            })
        return price