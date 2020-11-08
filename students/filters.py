import django_filters

from students.models import Students


class StudentsFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')
    email = django_filters.CharFilter(field_name='email',lookup_expr='icontains')
    first_name = django_filters.CharFilter(field_name='first_name',lookup_expr='icontains')
    last_name = django_filters.CharFilter(field_name='last_name',lookup_expr='icontains')

    class Meta:
        model = Students
        fields = ['first_name', 'last_name','email']