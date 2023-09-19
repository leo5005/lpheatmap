import django_filters
from .models import Data_Search


class DataSearchFilter(django_filters.FilterSet):
    class Meta:
        model = Data_Search
        fields = ['date_field', 'datetime_field']