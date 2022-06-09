import pyodbc


def store(username,password,user_email,phone):
	conn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=KALA_BHAALU\SQLEXPRESS;"
                      "Database=MAJOR_PROJECT;"
                      "Trusted_Connection=yes;")
	cursor = conn.cursor()
	
	query='''INSERT INTO USER_DATA (USERNAME,USER_PASSWORD,USER_EMAIL,PHONE) VALUES ('{}','{}','{}',{})'''.format(username,password,user_email,phone)
	cursor.execute(query)
#cursor.execute('DELETE FROM USER_DATA')
	conn.commit()
	cursor.close()
	conn.close()

#for row in cursor:
#   print('row = %r' % (row,))
def check(emailid,phone):
	conn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=KALA_BHAALU\SQLEXPRESS;"
                      "Database=MAJOR_PROJECT;"
                      "Trusted_Connection=yes;")
	cursor=conn.cursor()
	cursor.execute('SELECT * FROM USER_DATA')
	for i in cursor:
		if i[3]==emailid or i[4]==phone:                                        # removed lower()
			cursor.close()
			conn.close()
			return False
		else:
			pass
	else:
		cursor.close()
		conn.close()
		return True


def login_check(email_id,password):
	conn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=KALA_BHAALU\SQLEXPRESS;"
                      "Database=MAJOR_PROJECT;"
                      "Trusted_Connection=yes;")
	cursor=conn.cursor()
	cursor.execute('SELECT * FROM USER_DATA')
	for i in cursor:
		if i[3]==email_id:# # and i[2]==password:
			if i[2]==password:

				cursor.close()
				conn.close()
				return [True,i[0],0]
			else:
				cursor.close()
				conn.close()
				return [False,None,2]    # if password is incorrect

		else:
			pass
	else:
		cursor.close()
		conn.close()
		return [False,None,1]    # if email id is incorrect




def store_orders(cart,id1):
	conn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=KALA_BHAALU\SQLEXPRESS;"
                      "Database=MAJOR_PROJECT;"
                      "Trusted_Connection=yes;")
	cursor=conn.cursor()
	for t in cart:
		query="INSERT INTO ORDERS (CUSTOMER_ID,AMOUNT_PAID,ORDER_DATE,IMAGE_SRC,ORDER_NAME) VALUES ({},'{}',GETDATE(),'{}','{}')".format(id1,t[2],t[1],t[0])    # incorrect syntax here probably string
		cursor.execute(query)
	conn.commit()
	cursor.close()
	conn.close()


def retrieve_list(user_id1):
	conn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=KALA_BHAALU\SQLEXPRESS;"
                      "Database=MAJOR_PROJECT;"
                      "Trusted_Connection=yes;")
	cursor=conn.cursor()
	list_of_items=[]
	cursor.execute('''SELECT * FROM ORDERS WHERE CUSTOMER_ID = {}'''.format(user_id1))
	for u in cursor:
		tempt=[u[4],u[5],u[3],u[2]]           #img, name , date, price
		list_of_items.append(tempt)
	return list_of_items









