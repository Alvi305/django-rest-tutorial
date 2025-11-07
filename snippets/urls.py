from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from snippets import snippet_views

urlpatterns = [
    path("snippets/",snippet_views.SnippetList.as_view()),
    path("snippets/<int:pk>/", snippet_views.SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
