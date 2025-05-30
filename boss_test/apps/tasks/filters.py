from rest_framework.filters import OrderingFilter, SearchFilter


class CustomOrderingFilter(OrderingFilter):
    ordering_description = "Поле для сортировки"


class TaskSearchFilter(SearchFilter):
    search_param = 'q'
