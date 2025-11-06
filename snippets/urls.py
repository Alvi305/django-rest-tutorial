from django.urls import path
from snippets import snippet_views

urlpatterns = [
    path("snippets/", snippet_views.snippet_list),
    path("snippets/<int:pk>/", snippet_views.snippet_detail),
]