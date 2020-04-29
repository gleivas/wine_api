import django_filters

from wine_reviews.models import Wine

class WineFilter(django_filters.FilterSet):
    description = django_filters.CharFilter(lookup_expr='contains')
    price_gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    price_lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt')
    points_gt = django_filters.NumberFilter(field_name='points', lookup_expr='gt')
    points_lt = django_filters.NumberFilter(field_name='points', lookup_expr='lt')

    class Meta:
        model = Wine
        fields = ['country', 'variety', 'price', 'points']