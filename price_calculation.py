def calculate_it(cart):
	try:
		total=0
		for i in cart:
			temp=i[2][3::]
			temp1=temp.replace(',','')
			total=total+float(temp1)
		return ('Rs. '+str(total))
	except Exception:
		return 'an error occured, sorry for the inconvenience'
