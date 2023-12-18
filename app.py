from flask import Flask, render_template,request
from singleton import  Dbconnectivity

app = Flask(__name__)
# Singleton pattern object
connect = Dbconnectivity()
@app.route("/")
def index():
    return render_template("first.html")

@app.route("/first_form",methods = ["Get","post"])
def first_form():
    try:
        if(request.method == "POST"):
            button_clicked = request.form['button_clicked']
            print("hi")
            if button_clicked == 'button1':
                # Processing for the first button click
                return render_template("User/login_user.html")
            # if button_clicked == 'button2':
            #     # Processing for the second button click
            #     return render_template("doctor_1.html")
    except Exception as e:
        return f"Error :{e}!\nPlease Contact Developers"
    return "INVALID REQUEST"
    
@app.route("/signin_form",methods=['POST','GET'])
def signin_form():
    try:
        if(request.method == "POST"):
            link = request.form['button_clicked']
            if(link == 'btn1'):
                return render_template("User/direct.html")
    except Exception as e:
        return f"Error :{e}!\nPlease Contact Developers"
    return "INVALID REQUEST"

@app.route("/get_signup_page")
def get_signup_page():
    return render_template("/User/signup.html")

@app.route("/signup_form", methods=['POST', 'GET'])
def signup_form():
    global connect
    try:
        if(request.method == "POST"):
            button_clicked = request.form['button_clicked']
            print("hi")
            
            if button_clicked == 'btn1':
                u_id = request.form['id']
                u_name = request.form['user_name']
                password = request.form['password']
                email = request.form['email']
                phone = request.form['phone_number']
                print(u_id,u_name,type(phone))
                # Storing values through a single object
                connect.insert_user(u_id,u_name,password,email,phone)
                return render_template("/User/login_user.html")
            if button_clicked == 'btn2':
                # Processing for the second button click
                return render_template("/User/login_user.html")
    except Exception as e:
        return f"Error :{e}!\nPlease Contact Developers"
    return "INVALID REQUEST"

@app.route("/direct_form",methods = ['POST','GET'])
def direct_form():
    try:
        if(request.method == "POST"):
            button_clicked = request.form['button_clicked']
            if button_clicked == 'btn1':
                # Processing for the first button click
                return render_template("/User/book.html")
            if button_clicked == 'btn2':
                # Processing for the second button click
                return render_template("/User/user_log.html")
    except Exception as e:
        return f"Error :{e}!\nPlease Contact Developers"
    return "INVALID REQUEST"

@app.route("/book_form",methods = ['POST','GET'])
def book_form():
    try:
        if(request.method == "POST"):
            button_clicked = request.form['button_clicked']
            if button_clicked == 'btn1':
                # Processing for the first button click
                return render_template("/User/payment.html")
            
    except Exception as e:
        return f"Error :{e}!\nPlease Contact Developers"
    return "INVALID REQUEST"
    
if __name__ == "__main__":
    app.run(debug = True)