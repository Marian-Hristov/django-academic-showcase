from django.shortcuts import render
from .forms import MessagingForm

# Create your views here.

def send_message(request):
    f = MessagingForm()

    return render(request, 'messaging_app/messaging.html', {'form': f})