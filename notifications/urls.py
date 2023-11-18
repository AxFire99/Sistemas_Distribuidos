from django.urls import path
from .views import send_notification

urlpatterns = [
    path('send-notification/<str:username>/', send_notification, name='send_notification'),
]
