from django.urls import path

from .views import StatAPIView

urlpatterns = [
    path("", StatAPIView.as_view(), name="stat_list")
]