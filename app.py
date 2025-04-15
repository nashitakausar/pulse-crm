from flask import Flask, render_template, request, redirect, flash, session
#Importing the neccessary flask modules

import mysql.connector
#Importing mysql connector to connect python to SQL database

app = Flask(__name__)
#Creating a Flask web app instance
app.secret_key = 'simplecrmkey'


#Database connection
db = mysql.connector.connect(
    host = "localhost",
    user = "CRM_user",
    password = "nash1912",
    database = "simple_crm")

#Creating cursor object to execute SQL commands
cursor = db.cursor()

@app.route('/') #defining what happens when visiting homepage

def home():
    return render_template('home.html')
#Shows welcome message when visiting home page

@app.route('/customers')

def customers():
    cursor.execute("SELECT * FROM customers") #fetches all customers from database
    customer_list = cursor.fetchall() #gets all rows from the query
    return render_template('customers.html', customers=customer_list) #renders an html page and pass the customer data into it

@app.route('/add-customer', methods=["GET", "POST"]) #GET to show form and POST to submit form

def add_customer():
    if request.method == "POST": #if form was submitted
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        company = request.form['company']
        notes = request.form['notes']

        cursor.execute("INSERT INTO customers (customer_name, email, phone, company, notes) VALUES (%s, %s, %s, %s, %s)",
                       (name, email, phone, company, notes))
        db.commit()
        
        flash('➕ Customer added successfully!')
        return redirect('/customers') #redirect to customers after saving
    
    #just show the form if it is a GET request
    return render_template('add_customer.html')

@app.route('/delete-customer/<int:customer_id>', methods=['POST'])

def delete_customer(customer_id):
    cursor.execute("DELETE FROM customers WHERE customer_id = %s", (customer_id,))
    db.commit()

    flash('➖ Customer deleted successfully!')
    return redirect('/customers')

@app.route('/edit-customer/<int:customer_id>', methods=['GET', 'POST'])

def edit_customer(customer_id):
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        company = request.form['company']
        notes = request.form['notes']

        cursor.execute("UPDATE customers SET customer_name=%s, email=%s, phone=%s, company=%s, notes=%s WHERE customer_id=%s",
                       (name, email, phone, company, notes, customer_id))
        db.commit()

        flash('✏️ Customer details updated successfully!')
        return redirect('/customers')
    else:
        cursor.execute("SELECT * FROM customers WHERE customer_id=%s", (customer_id,))
        customer = cursor.fetchone()
        return render_template('edit_customer.html', customer=customer)
        

if __name__ == '__main__':
    app.run(debug=True)
    #Starts Flask web server in debug mode (auto-restarts on changes)
