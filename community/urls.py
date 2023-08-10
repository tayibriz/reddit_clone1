from django.urls import path
from .views import CommunityView

urlpatterns = [
    # ... Other URL patterns
    path("community/", CommunityView.as_view(), name="community"),
    
]
