from .email import sendEmail
import time

providerList = [
	'@txt.att.net', #ATT
	'@vtext.com', #Verizon
	'@tmomail.net', #T-Mobile
	'@messaging.sprintpcs.com', #Sprint
	'@vmobl.com', #Virgin Mobile
]

def spamText(numTexts, phone_number, message, email):
	for x in range(int(numTexts)):
		for provider in providerList:
			emailPerson = phone_number + provider
			sendEmail(email, emailPerson, message)
			time.sleep(.1)
