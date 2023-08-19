import smtplib, ssl

def sendEmail(message):
	smtp_server = "smtp.gmail.com"
	port = 587 
	sender_email = "rkallakkavumkel@gmail.com"
	password = "GilsAnna"
	receiver_email = "roshankallakkavumkel@gmail.com"

	context = ssl.create_default_context()
	try:
		server = smtplib.SMTP(smtp_server,port)
		server.starttls(context=context) 
		'''
		Using StartTLS, an email client can inform the email
		server that it wants to upgrade from an insecure to
		secure connection using TLS or SSL
		'''
		server.login(sender_email,password) #serve.login” tries to log into that particular id
		server.sendmail() # it will send an email on the mentioned email addresses
	except Exception as e:
		print(e)
		
	finally:
		server.quit()

