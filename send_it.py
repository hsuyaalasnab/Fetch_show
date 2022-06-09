import smtplib

def sending_mail(OTP,emailed):
	smtpObj = smtplib.SMTP('smtp.gmail.com',587)
	smtpObj.ehlo()
	smtpObj.starttls()
	smtpObj.login('aayushbansal1998.ab@gmail.com', '9213322030')
	smtpObj.sendmail('aayushbansal1998.ab@gmail.com',emailed,'Your OTP is '+str(OTP))
	smtpObj.quit()