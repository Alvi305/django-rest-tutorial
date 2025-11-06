from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from snippets import snippet_views

urlpatterns = [
    path("snippets/", snippet_views.snippet_list),
    path("snippets/<int:pk>/", snippet_views.snippet_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
