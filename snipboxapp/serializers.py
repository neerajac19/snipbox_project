from rest_framework import serializers
from .models import Snipbox, Tag

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snipbox
        fields = ['id', 'title', 'note', 'created_at', 'updated_at','user', 'tags']
