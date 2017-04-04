from rest_framework import serializers
from .models import Link


class LinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Link
        fields = ('title', 'clicks')

# class LinkSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField()
#     clicks = serializers.IntegerField()
#
#     def create(self, validated_data):
#         return Link.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.clicks = validated_data.get('clicks', instance.clicks)
#         instance.save()
#         return instance
