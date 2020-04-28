from rest_framework import serializers
from crawl.models import Links


class LinksSerializer(serializers.ModelSerializer):
    class Meta :
        model = Links
        fields = ['id', 'title', 'url', 'source']

    def create(self, validated_data):
        """
        Create and return a new `Link` instance, given the validated data.
        """
        return Links.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.url = validated_data.get('url', instance.url)
        instance.source = validated_data.get('source', instance.source)
        instance.save()
        return instance