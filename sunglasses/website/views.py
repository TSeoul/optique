from django.shortcuts import render
from django.core.mail import send_mail



from django.http import HttpResponse
from django.core import serializers
from .models import Lunettes


def shop(request):
    lunettes = Lunettes.objects.all()
    return render(request, "shop.html", {'lunettes': lunettes})

def home(request):
    return render(request, "home.html", {})


def contact(request):
    if request.method == "POST":
        name = request.POST['Name']
        phone_number = request.POST['Phone Number']
        email = request.POST['email']
        message = request.POST['Message']

        # send an email
        send_mail(
            'message du site internet',# subject
            message, # message
            email, # from email
            ['tm.sallerin@gmail.com'], # To email
        )


        return render(request, "contact.html", {'name': name})

    else:
        return render(request, "contact.html", {})


def about(request):
    return render(request, "about.html", {})

def glasses(request):
    lunettes = Lunettes.objects.all()
    return render(request, "glasses.html", {'lunettes': lunettes})




def api_get_lunettes(request):
    lunettes = Lunettes.objects.all()
    json = serializers.serialize("json", lunettes)
    return HttpResponse(json)