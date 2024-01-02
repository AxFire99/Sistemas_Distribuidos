# notifications/views.py
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import UserSelectForm
from django.urls import reverse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from .serializers import EventNotificationSerializer, PaymentNotificationSerializer

def index(request):
    return render(request, 'index.html')

def select_user(request):
    if request.method == 'POST':
        form = UserSelectForm(request.POST)
        if form.is_valid():
            selected_user = form.cleaned_data['user']
            return redirect(reverse('send_notification', args=[selected_user.username]))
    else:
        form = UserSelectForm()

    return render(request, 'notification.html', {'form': form})

def send_notification(request, username):
    user = User.objects.get(username=username)
    subject = 'Notification from Your Django App'
    message = 'This is a notification email from your Django app.'
    from_email = 'sendernotification490@gmail.com'  # Replace with your email
    recipient_list = [user.email]

    html_message = render(request, 'notifications/email_template.html', {'user': user}).content.decode('utf-8')

    send_mail(subject, message, from_email, recipient_list, html_message=html_message)

    return render(request, 'notification_sent.html')


def users(request):
    #pull data from third party rest api
    #response = requests.get('https://jsonplaceholder.typicode.com/users')
    #convert reponse data into json
    #users = response.json()

    users = User.objects.all()
    print(users)
    return render(request, "users.html", {'users': users})
    pass

class NotificationAPIView(APIView):
    def post(self, request, *args, **kwargs):
        notification_type = request.data.get('notification_type')

        if notification_type == 'event':
            serializer = EventNotificationSerializer(data=request.data)
        elif notification_type == 'payment':
            serializer = PaymentNotificationSerializer(data=request.data)
        else:
            return Response({'error': 'Invalid notification_type'}, status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():
            email = serializer.validated_data['email']

            # Send the email based on the notification type
            if notification_type == 'event':
                event_date_time = serializer.validated_data['event_date_time']
                event_name = serializer.validated_data['event_name']
                event_location = serializer.validated_data['event_location']
                subject = 'Event Reminder'
                body = f'This is an reminder notification for your {event_name} event scheduled on {event_location} at {event_date_time}.\nDo not forget to get ready for it and most importantly, We hope you enjoy your time there.'

            elif notification_type == 'payment':
                payment_event_name = serializer.validated_data['payment_event_name']
                payment_date_time = serializer.validated_data['payment_date_time']
                subject = 'Payment Successful'
                body = f'This is a payment notification to confirm you that your payment for {payment_event_name} was succesfully received at {payment_date_time}. \nYou will also receive a notification when it is closer to the date of the event so that you dont forget.\nWe hope you enjoy your event!'

            # Send the email
            send_mail(
                subject,
                body,
                'from@example.com',
                [email],
                fail_silently=False,
            )

            return Response({'message': 'Notification sent successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)