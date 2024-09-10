from django.shortcuts import render, redirect
from .models import Meetup, Participant
from .forms import RegistrationForm
# Create your views here.

#a view is a simple python function 

def index(request):
    meetups = Meetup.objects.all()
    return render(request, 'meetups/index.html', {
        'meetups':meetups,})
# render = prepares templates and enriches them with data and generates final html content to return to request in browser and requires 2 arguments


def details(request, meetup_slug):
    try:
        SELECTED_MEETUP= Meetup.objects.get(slug=meetup_slug)
        if request.method == 'GET':
            registration_form = RegistrationForm()
        else:
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid(): 
                user_email = registration_form.cleaned_data['email']
                participant, _ = Participant.objects.get_or_create(email=user_email)
                SELECTED_MEETUP.participants.add(participant)
                return redirect('confirm-reg', meetup_slug=meetup_slug)




        return render(request, 'meetups/details.html', {
                'meetup_found': True,
                'meetup': SELECTED_MEETUP, 
                'form': registration_form,
        })
    except Exception as exc: 
        return render(request, 'meetups/details.html',
              {'meetup_found': False
         })
    


def confirm_registration(request, meetup_slug):
    meetup= Meetup.objects.get(slug=meetup_slug)
    return render(request, 'meetups/confirmation.html', {
        'organizer_email': meetup.organizer_email


    })