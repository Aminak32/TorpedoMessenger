from django.contrib import admin

from .forms import PhoneNumbersForm
from .models import PhoneNumbers

# Register your models here.

class PhoneNumbersAdmin(admin.ModelAdmin):
	list_display = ["email",
					"phone_number",
					"amount_to_send",
					"message",
					"ipAddress",
					"timestamp",]
	form = PhoneNumbersForm

admin.site.register(PhoneNumbers, PhoneNumbersAdmin)
