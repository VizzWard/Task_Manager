from rest_framework.pagination import LimitOffsetPagination

class CustomTasksLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 15