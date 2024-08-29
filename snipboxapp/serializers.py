from rest_framework import serializers
from .models import Snipbox, Tag

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snipbox
        fields = ['id', 'title', 'note', 'created_at', 'updated_at', 'tags']



class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'title']


class SnippetOverviewSerializer(serializers.ModelSerializer):
    detail_url = serializers.HyperlinkedIdentityField(view_name='snippet-detail', lookup_field='pk')

    class Meta:
        model = Snipbox
        fields = ['title', 'note', 'created_at', 'detail_url']

