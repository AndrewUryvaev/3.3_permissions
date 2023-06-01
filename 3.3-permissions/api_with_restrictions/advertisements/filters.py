from django_filters import rest_framework as filters

from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    class Meta:
        model = Advertisement
        fields = ['title', 'status', 'created_at']
