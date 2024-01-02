# serializers.py
from rest_framework import serializers

class EventNotificationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    notification_type = serializers.CharField()
    event_date_time = serializers.DateTimeField()
    event_name = serializers.CharField()
    event_location = serializers.CharField()

class PaymentNotificationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    payment_event_name = serializers.CharField()
    payment_date_time = serializers.DateTimeField()
    notification_type = serializers.CharField()

# We can add more serializers for different notification types if needed