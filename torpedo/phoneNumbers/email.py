import smtplib
import time

#########
#Python 3
#########

def sendEmail(FROM, TO, TEXT):
	SERVER = "localhost"
	
	message = TEXT
	
	try:
		server = smtplib.SMTP(SERVER)
		server.sendmail(FROM, TO, message)
		server.quit()
	
	except:
		print("Failure, check to make sure the email server is on.")
