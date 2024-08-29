from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Snipbox, Tag
from .serializers import SnippetSerializer
from rest_framework.permissions import IsAuthenticated
from .serializers import TagSerializer, SnippetOverviewSerializer
from django.shortcuts import get_object_or_404
#import logging

#logger = logging.getLogger(__name__)

class SnippetCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        data = request.data
        
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




class SnippetDeleteView(generics.DestroyAPIView):
    queryset = Snipbox.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        remaining_snippets = self.get_queryset()
        serializer = SnippetSerializer(remaining_snippets, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    


class TagListView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticated]


class TagDetailView(generics.ListAPIView):
    serializer_class = SnippetSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        tag = Tag.objects.get(pk=self.kwargs['pk'])
        return Snipbox.objects.filter(tags=tag, user=self.request.user)
    
    
class SnippetOverviewView(generics.GenericAPIView):
    serializer_class = SnippetOverviewSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        snippets = Snipbox.objects.filter(user=self.request.user)
        total_count = snippets.count()
        serializer = self.get_serializer(snippets, many=True)
        data = {
            'total_count': total_count,
            'snippets': serializer.data
        }
        return Response(data)
    
class SnippetDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk, *args, **kwargs):
        snippet = get_object_or_404(Snipbox, pk=pk, user=request.user)
        snippet_serializer = SnippetSerializer(snippet)
        return Response(snippet_serializer.data, status=status.HTTP_200_OK)


class SnippetUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk, *args, **kwargs):
        snippet = get_object_or_404(Snipbox, pk=pk, user=request.user)
        print(f"Fetching Snippet with pk: {pk}")
        data = request.data
        
        tags_data = data.pop('tags', [])

        tags = []
        for tag_title in tags_data:
            tag, created = Tag.objects.get_or_create(title=tag_title)
            tags.append(tag)

        snippet_serializer = SnippetSerializer(snippet, data=data, partial=True)
        if snippet_serializer.is_valid():
            snippet = snippet_serializer.save()
            snippet.tags.set(tags)  
            return Response(snippet_serializer.data, status=status.HTTP_200_OK)
        return Response(snippet_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
