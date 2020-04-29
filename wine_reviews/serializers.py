from rest_framework import serializers

from wine_reviews.models import Wine


class WineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Wine
        fields = '__all__'
