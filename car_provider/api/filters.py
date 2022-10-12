import django_filters


class BrandFilter(django_filters.FilterSet):
    brand = django_filters.CharFilter(
        field_name='car__brand__brand',
    )
