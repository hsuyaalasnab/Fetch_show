from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
import product_scrapper


app = Flask(__name__)   #this __name__ variable takes in the name of the file


@app.route('/', methods=['GET', 'POST'])
def index():
    products = []
    if request.method == "POST":
      query = request.form.get("query")
      products = product_scrapper.scrap(query)
    return render_template('scrapper.html', products = products)


if __name__ == "__main__":
    app.secret_key=os.urandom(16)
    app.run(debug=True,host='0.0.0.0', port=5959)