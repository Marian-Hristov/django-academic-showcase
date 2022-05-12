from django.shortcuts import render, redirect
from .forms import MessagingForm
from user_management.models import Profile
from .models import Message
# Create your views here.

def get_user_profile(name):
    for prof in Profile.objects.all():
        if(prof.user.username == name):
            return prof

def send_message(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            f = MessagingForm(request.POST)
            if f.is_valid():
                body, username = f.get_data()
                recipient_profile = get_user_profile(username)
                sender_profile = get_user_profile(request.user.username)
                new_message = Message(
                    body=body,
                    receiver=recipient_profile,
                    sender=sender_profile
                )
                new_message.save()

                for elem in Message.objects.all():
                    print(f'{elem.sender.user.username} sent a message to {elem.receiver.user.username} that said: {elem.body}')
        else:
            f = MessagingForm()
        return render(request, "user_messaging/messaging.html", {'form': f})
    else:
        return redirect('dashboard')
