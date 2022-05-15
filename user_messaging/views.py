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

                return redirect('view-messages')
        else:
            f = MessagingForm()
        return render(request, "user_messaging/send_messages.html", {'form': f})
    else:
        return redirect('dashboard')

def view_messages(request):
    if request.user.is_authenticated:
        context = {'messages': None, 'has_msg': True}
        users_messages = []
        for msg in Message.objects.all():
            if msg.sender.user.username == request.user.username or msg.receiver.user.username == request.user.username:
                if msg.receiver.user.username == request.user.username:
                    Message.objects.filter(pk=msg.pk).update(read_receiver=True)
                    msg.read_receiver = True
                msg.sender.avatar = bytes(msg.sender.avatar).decode()
                msg.receiver.avatar = bytes(msg.receiver.avatar).decode()
                users_messages.append(msg)
        if len(users_messages) == 0:
            context['has_msg'] = False
            return render(request, 'user_messaging/view_messages.html', context=context)
        context['messages'] = users_messages
        return render(request, 'user_messaging/view_messages.html', context=context)
    else:
        return redirect('dashboard')
