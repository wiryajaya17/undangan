from django.shortcuts import render
from .models import Rsvp
from datetime import datetime

def twainlove(request):
    # rsvps = Rsvp.objects.filter(name='Wirwir')
    # rsvps = Rsvp.objects.post_date__gte=datetime.date.today()
    rsvps = Rsvp.objects.filter(owner='twainlove').order_by('-post_date')
    return render(request, 'twainlove.html', {'rsvps' : rsvps})

def create(request):
    if request.method == 'POST':
        rsvp = Rsvp()
        rsvp.owner = 'twainlove'
        rsvp.name = request.POST['name']
        rsvp.email = request.POST['email']
        rsvp.num_of_rsvp = request.POST['num_of_rsvp']
        rsvp.flag_attending = request.POST['flag_attending']
        rsvp.message_body = request.POST['message_body']
        rsvp.save()
        return render(request,'create.html', {})
    else:
        return render(request, 'twainlove.html', {})
    # return render(request,'create.html', {})
