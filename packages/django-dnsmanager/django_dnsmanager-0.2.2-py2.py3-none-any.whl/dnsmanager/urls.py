from django.urls import path

from .views import ZoneDetailView

urlpatterns = [
    path('<slug:slug>/', ZoneDetailView.as_view(content_type='text/plain'), name='zone-detail'),
]
