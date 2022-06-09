













from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
import store_sql
import OTP
import product_scrapper
import routing
import price_calculation

otp_generated=None
cart=[]
products=[]
line1=None
line2=None
line3=None
user_id=None

app = Flask(__name__)



@app.route('/orders', methods=['GET','POST'])
def user_orders():
    if session['logged_in']==True:
        global user_id
        order_item_list=store_sql.retrieve_list(user_id)
        
        return render_template('previous_order.html',order_parchi=order_item_list)
    else:
        return home()




@app.route('/OTP', methods=['GET','POST'])
def otp_verify():
    if session['logged_in']==False:
        if request.method == 'POST':
            global otp_generated
            otp_to_be_checked=request.form["user_otp"]
        
        #return '<h1>{} {}</h1>'.format(str(otp_generated),str(otp_to_be_checked))
            if str(otp_to_be_checked)==str(otp_generated):
                session['logged_in'] = True
                global cart,products
                cart=[]
                products=[]
                return index()
            else:
                session['logged_in']==False
                return render_template('login1.html',flag=3)
    else:
        return home()
        #return render_template('otp_verification.html')
    


@app.route('/add',methods=['GET','POST'])
def add():
    global cart
    if request.method=="POST":
        temp=request.form.get("code")
        #temp1=request.form.get("quantity")
        temp2=request.form.get("image")
        temp3=request.form.get("price")
        cart.append([temp, temp2,temp3])
        global products
        return render_template('scrapper_1.html',products=products,carts=cart)


@app.route('/scrap', methods=['GET', 'POST'])
def index():
    if session['logged_in']==True:
    
        if request.method == "POST":
            query = request.form.get("query")
            global products
            global cart
            products = product_scrapper.scrap(query)
        return render_template('scrapper_1.html', products = products,carts=cart )
    else:
        return do_login()



@app.route('/results',methods=['POST','GET'])
def results():
    if session["logged_in"]==True:
        sum_amount=0
        global cart
        
        if session['logged_in']==True:
            if request.method=="POST":
                deletion=request.form.get("code1")
                deletion=int(deletion)
                cart.pop(deletion)


        total_amount=price_calculation.calculate_it(cart)
        return render_template('results.html', products=cart,total_amount=total_amount) 
    else:
        return do_login()


@app.route('/',methods=['GET', 'POST'])
def home():
    if not session.get('logged_in'):
        if request.method=="POST":
            username=request.form.get('new_username')
            password=request.form.get('password')
            email_id=request.form.get('email_id')
            phone=request.form.get('contact')
            if store_sql.check(email_id,phone)==True:
            	store_sql.store(username,password,email_id,phone)
            	return render_template('login1.html')
            else:
            	return render_template('registration1.html')

    session['logged_in']=False      
    return render_template('registration1.html')

    #else:
    #    return index()
@app.route('/login', methods=['GET','POST'])
def do_login():
    try:
        if request.method =='POST':
            username=request.form.get('email')
            password=request.form.get('password1')
            checking_it=store_sql.login_check(username,password)
            if checking_it[0]==True:
                
                global otp_generated
                global user_id
                user_id=checking_it[1]
                otp_generated=OTP.otp_manager(username)
                #return otp_verify()
                return render_template('otp_verification.html')
            else:
                return render_template('login1.html',flag=checking_it[2])
        session['logged_in']=False 
        return render_template('login1.html',flag=0)
    except RecursionError:
        return home()
    except IndexError:
        return home() 	


@app.route('/checkout',methods=['POST','GET'])
def checkout():
    global line1,line2,line3
    line1=None
    line2=None
    line3=None
    if session['logged_in']==True:
        
        if request.method=="POST":
            line1=request.form.get('line1')
            line2=request.form.get('line2')
            line3=request.form.get('line3')
            global user_id
            global cart
            store_sql.store_orders(cart,user_id)
            cart=[]
            return render_template('final.html')
        return render_template('checkout.html')

    else:
        return home()

@app.route('/directions',methods=['POST','GET'])
def directions():
    routing.give_directions(line1,line2,line3)
    return render_template('final.html')


if __name__ == "__main__":

    app.secret_key=os.urandom(16)
    app.run(debug=True,host='0.0.0.0', port=5959)