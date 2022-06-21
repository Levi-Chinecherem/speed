from django.shortcuts import render, redirect
from .models import Subscriber, Contact


# Home View
def home_view(request):
    subscribers = Subscriber()
    if request.method == 'POST':
        email = request.POST.get('email')
        if email and email != '':
            subscribers = Subscriber(email=email)
            subscribers.save()
            return redirect("home")
    return render(request, 'index.html')

# About View
def about_view(request):
    return render(request, 'about.html')

# Contact View
def contact_view(request):
    return render(request, 'contact.html')

# Gallery View
def gallery_view(request):
    return render(request, 'gallery.html')

# Testimonial View
def testimonial_view(request):
    return render(request, 'testimonial.html')


#Get the contact details
def getContact(request):
    contact = Contact
    name = request.POST.get('name')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    message = request.POST.get('message')
    contact = Contact(name=name, email=email, phone=phone, message=message)
    contact.save()
    return redirect("home")