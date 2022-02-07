from django.shortcuts import render
from yayarani.models import Rsvp
from datetime import datetime

def theme2(request):
    # rsvps = Rsvp.objects.filter(name='Wirwir')
    # rsvps = Rsvp.objects.post_date__gte=datetime.date.today()
    rsvps = Rsvp.objects.filter(owner='twainlove').order_by('-post_date')
    return render(request, 'theme2.html', {'rsvps' : rsvps})

def create2(request):
    if request.method == 'POST':
        rsvp = Rsvp()
        rsvp.owner = 'twainlove'
        rsvp.name = request.POST['name']
        rsvp.email = ''
        rsvp.num_of_rsvp = 1
        rsvp.flag_attending = request.POST['flag_attending']
        rsvp.message_body = request.POST['message_body']
        rsvp.save()
        return render(request,'create2.html', {})
    else:
        return render(request, 'theme2.html', {})
    # return render(request,'create.html', {})
