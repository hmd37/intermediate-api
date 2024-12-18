from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from books.models import Book, Comment
from .serializers import BookSerializer, CommentSerializer

#Concrete views
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView

#Permissions
from rest_framework import permissions
from books.api.permissions import IsAdminOrStaffReadOnly, IsCommentOwnerOrReadOnly
from books.api.pagination import SmallPagination, LargePagination

from rest_framework.exceptions import ValidationError


class BookListCreateAPIView(ListCreateAPIView):
    queryset = Book.objects.order_by('-id')
    serializer_class = BookSerializer
    permission_classes = [IsAdminOrStaffReadOnly]
    pagination_class = SmallPagination


class BookDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminOrStaffReadOnly]


class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        book_id = self.kwargs.get('book_id')

        check_comments = Comment.objects.filter(book=book_id, owner_of_comment=self.request.user)

        if check_comments.exists():
            raise ValidationError("You can't make more than 1 comment on a book!")

        serializer.save(book_id=book_id, owner_of_comment=self.request.user)

class CommentDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsCommentOwnerOrReadOnly]


# class BookListCreateAPIView(ListModelMixin, CreateModelMixin, GenericAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
