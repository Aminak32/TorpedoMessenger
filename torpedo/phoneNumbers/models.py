from django.db import models

# Create your models here.

class PhoneNumbers(models.Model):
	email = models.EmailField()
	phone_number = models.CharField(max_length = 12)
	amount_to_send = models.CharField(max_length = 10)
	message = models.CharField(max_length = 100)
	ipAddress = models.CharField(max_length = 20)
	timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)

	def __unicode__(self): #If python 3 then __str__
		return self.email
