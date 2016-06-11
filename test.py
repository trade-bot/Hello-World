import smtplib

sender = 'sau.ag01@gmail.com'
receivers = ['eb31rahul@gmail.com']

message = """From: From Person <sau.ag01@gmail.com>
To: To Person <eb31rahul@gmail.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, receivers, message)         
   print "Successfully sent email"
except SMTPException:
   print "Error: unable to send email"