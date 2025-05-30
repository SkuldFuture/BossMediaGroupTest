from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.pagination import PageNumberPagination


class CustomSearchFilter(SearchFilter):
    search_description = "Поиск"


class CustomPagination(PageNumberPagination):
    page_size = 10
    max_page_size = 100000
    page_query_param = "page"
    page_query_description = "Номер страницы"
    page_size_query_param = "page_size"
    page_size_query_description = "Размер страницы"
