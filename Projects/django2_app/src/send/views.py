from django.shortcuts import render
from django.core.mail import send_mail

def index(request):
    send_mail(
        'Hello from Hasan',
        'This is the body of email',
        '',
        [''],
        fail_silently=False
    )
    return render(request, 'email.html')
