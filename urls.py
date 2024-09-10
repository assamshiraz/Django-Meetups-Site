from django.urls import path 
from . import views
#import file views.py


urlpatterns = [
    path('meetups/', views.index, name='all-meetups'), #our-domain.com/meetups
    path('meetups/<slug:meetup_slug>/success', views.confirm_registration, name='confirm-reg'),
    path('meetups/<slug:meetup_slug>', views.details, name='meetup-detail'), #ourdoamin.com/meetups/dyanmic meetupname
]   