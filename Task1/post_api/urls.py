from django.urls import path
from .views import JsonAPICreateView, OwnerAPIView, CampaigneAPIView, URLAPIView, GetURLDetailsView


urlpatterns = [
    path('upload', JsonAPICreateView.as_view()),
    path('owner', OwnerAPIView.as_view()),
    path('campaign', CampaigneAPIView.as_view()),
    path('urls',URLAPIView.as_view()),
    path('geturl', GetURLDetailsView.as_view())
]
