from django.urls import path

from .views import ContentDetailView, ContentFilterView, ContentView

urlpatterns = [
    path("contents/", ContentView.as_view()),
    path("contents/filter/", ContentFilterView.as_view()),
    path("contents/<content_id>/", ContentDetailView.as_view()),
    
]
