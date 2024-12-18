from rest_framework import pagination


class SmallPagination(pagination.PageNumberPagination):
    page_size = 6
    page_query_param = 'pg'

class LargePagination(pagination.PageNumberPagination):
    page_size = 10
    page_query_param = 'pg'