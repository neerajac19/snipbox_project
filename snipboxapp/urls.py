from django.urls import path
from .views import SnippetCreateView, SnippetDeleteView, TagListView, TagDetailView, SnippetDetailView, SnippetOverviewView, SnippetUpdateView


urlpatterns = [
    path('snippets/', SnippetCreateView.as_view(), name='snippet-create'),
    path('snippets/<int:pk>/delete/', SnippetDeleteView.as_view(), name='snippet-delete'),
    path('tags/', TagListView.as_view(), name='tag-list'),
    path('tags/<int:pk>/', TagDetailView.as_view(), name='tag-detail'),
    path('snippets/<int:pk>/', SnippetDetailView.as_view(), name='snippet-detail'),
    path('snippets/overview/', SnippetOverviewView.as_view(), name='snippet-overview'),
    path('snippets/<int:pk>/update/', SnippetUpdateView.as_view(), name='snippet-update'),

]


