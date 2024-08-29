from django.urls import path
from .views import SnippetCreateView, SnippetDeleteView, TagListView


urlpatterns = [
    path('snippets/', SnippetCreateView.as_view(), name='snippet-create'),
    path('snippets/<int:pk>/delete/', SnippetDeleteView.as_view(), name='snippet-delete'),
    path('tags/', TagListView.as_view(), name='tag-list'),

]
