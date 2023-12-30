from django.core.mail import send_mail
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
# notifications/views.py
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import UserSelectForm
from django.urls import reverse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from .serializers import NotificationSerializer

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
        serializer = NotificationSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']

            # Your notification logic here
            # For example, sending an email
            send_mail(
                'Testing',
                'This is a test message, If you have received this it means the testing is working. :)',
                'Notification Service',
                [email],
                fail_silently=False,
            )

            return Response({'message': 'Notification sent successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
