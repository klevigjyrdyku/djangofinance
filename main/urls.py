from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'finance'

urlpatterns = [
    path('register/', views.register, name='register'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


