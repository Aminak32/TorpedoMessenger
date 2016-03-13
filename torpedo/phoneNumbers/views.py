from django.shortcuts import render
from ipware.ip import get_ip

from .email import sendEmail
from .sendText import spamText
from .forms import ContactForm, PhoneNumbersForm

# Create your views here.

def home(request):
	ip = get_ip(request)
	
	form = PhoneNumbersForm(request.POST or None)
	
	if form.is_valid():
		instance = form.save(commit = False)
		instance.ipAddress = ip
		
		email = form.cleaned_data.get("email")
		amount_to_send = form.cleaned_data.get("amount_to_send")
		phone_number = form.cleaned_data.get("phone_number")
		message = form.cleaned_data.get("message")
	
		spamText(amount_to_send, phone_number, message, email)
		instance.save()

	context = {
		"ip_address": ip,
		"form": form,
	}
	
	return render(request, "home.html", context)

def contact(request):
	form = ContactForm(request.POST or None)
	
	if form.is_valid():
		email = form.cleaned_data.get("email")
		message = form.cleaned_data.get("message")
		sendEmail("contact@torpedo.com", ["dan.kirichok@gmail.com", "6038181498@messaging.sprintpcs.com"], str(email) + " " + str(message))
	
	context = {
		"form": form,
	}
	
	return render(request, "contact.html", context)
