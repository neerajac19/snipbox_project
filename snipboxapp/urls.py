from django.urls import path
from .views import SnippetCreateView

urlpatterns = [
    path('snippets/', SnippetCreateView.as_view(), name='snippet-create'),
    # Add other URLs here
]
