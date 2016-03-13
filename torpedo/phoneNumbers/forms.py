from django import forms

from .models import PhoneNumbers

class ContactForm(forms.Form):
	email = forms.EmailField()
	message = forms.CharField()

class PhoneNumbersForm(forms.ModelForm):
	class Meta:
		model = PhoneNumbers
		fields = ['email', 'amount_to_send', 'phone_number', 'message']

	
