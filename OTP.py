import random
import otp_testing
def otp_manager(email_id):
	a=random.randint(10,99)
	alphabets=[]
	for i in range(98,123):
		alphabets.append(chr(i))
	for j in range(65,91):
		alphabets.append(chr(j))
	b=random.choice(alphabets)
	c=random.choice(alphabets)
	d=random.randint(10,99)
	otp=str(a)+b+c+str(d)
	otp_testing.send_desired_email(otp,email_id)

	return otp