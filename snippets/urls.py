from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from snippets import snippet_views
# API endpoints
urlpatterns = format_suffix_patterns(
    [
        path("", snippet_views.api_root),
        path("snippets/", snippet_views.SnippetList.as_view(), name="snippet-list"),
        path(
            "snippets/<int:pk>/", snippet_views.SnippetDetail.as_view(), name="snippet-detail"
        ),
        path(
            "snippets/<int:pk>/highlight/",
            snippet_views.SnippetHighlight.as_view(),
            name="snippet-highlight",
        ),
        path("users/", snippet_views.UserList.as_view(), name="user-list"),
        path("users/<int:pk>/", snippet_views.UserDetail.as_view(), name="user-detail"),
    ]
)
