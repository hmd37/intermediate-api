from rest_framework import serializers
from books.models import Book, Comment


class CommentSerializer(serializers.ModelSerializer):
    owner_of_comment = serializers.StringRelatedField()
    class Meta:
        model = Comment
        exclude = ['book']

class BookSerializer(serializers.ModelSerializer):
    comments=CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = '__all__'