import django_filters
from django_filters import DateFilter, CharFilter
from .models import *

class OrderFilter(django_filters.FilterSet):
	from_date = DateFilter(field_name="date_created",lookup_expr='gte',label="from_date")
	to_date = DateFilter(field_name="date_created",lookup_expr='lte',label="to_date")
	note = CharFilter(field_name="note",lookup_expr='icontains')

	class Meta:
		model = Order
		fields = '__all__'
		exclude = ['customer','date_created']