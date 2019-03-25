#sending mail using python
import smtplib
try:
	s=smtplib.SMTP('smtp.gmail.com','587')
	s.starttls()
	sender=''
	receiver=''
	msg="hii"
	s.login(sender,'')
	s.sendmail(sender,receiver,msg)
except:
	print("some error occured")
else:
	print("msg sent successfully")
	s.quit()