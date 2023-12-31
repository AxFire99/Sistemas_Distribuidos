from django.urls import path
from .views import send_notification, users, select_user, NotificationAPIView

urlpatterns = [
    path('notification/', select_user, name='select_user'),
    path('send-notification/<str:username>/', send_notification, name='send_notification'),
    path('users/', users, name='users'),
    path('api/send-notification/', NotificationAPIView.as_view(), name='send-notification')
]
