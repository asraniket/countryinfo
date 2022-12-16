from rest_framework import serializers

class CountryInfoSerializer(serializers.Serializer):
    name = serializers.CharField()
    capital = serializers.CharField()
    population = serializers.IntegerField()
    area = serializers.FloatField()
    official_language = serializers.CharField()
