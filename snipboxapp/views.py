from rest_framework import status, generics, permisiions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Snipbox, Tag
from .serializers import SnippetSerializer
from rest_framework.permissions import IsAuthenticated

class SnippetCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        data = request.data
        print(data)
        tags_data = data.pop('tags', [])

        tags = []
        for tag_title in tags_data:
            tag, created = Tag.objects.get_or_create(title=tag_title)
            tags.append(tag)

        # Create the snippet
        snippet_serializer = SnippetSerializer(data=data)
        if snippet_serializer.is_valid():
            snippet = snippet_serializer.save(user=request.user)
            snippet.tags.set(tags)  
            return Response(snippet_serializer.data, status=status.HTTP_201_CREATED)
        return Response(snippet_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

