from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import Dashboard

urlpatterns = [
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
