from django.core.mail import send_mail
from django.shortcuts import render
from django.contrib.auth.models import User

def send_notification(request, username):
    user = User.objects.get(username=username)
    subject = 'Notification from Your Django App'
    message = 'This is a notification email from your Django app.'
    from_email = 'sendernotification490@gmail.com'  # Replace with your email
    recipient_list = [user.email]

    html_message = render(request, 'notifications/email_template.html', {'user': user}).content.decode('utf-8')

    send_mail(subject, message, from_email, recipient_list, html_message=html_message)

    return render(request, 'notifications/notification_sent.html')
