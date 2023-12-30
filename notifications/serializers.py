from rest_framework import serializers

class NotificationSerializer(serializers.Serializer):
    email = serializers.EmailField()