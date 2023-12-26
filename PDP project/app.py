from flask import Flask, render_template,request,json,jsonify
from singleton import  user,Picklestorage,Orders,owner
from observer import Book
from facade import Facade

app = Flask(__name__)
us_id = 0
table_no = 0
timing = 0
date = 0
t_type = 0
users_id = 0
owners_id = 0
# Singleton pattern object
store = Picklestorage()
f = Facade()


@app.route("/")
def index():
    return render_template("first.html")


@app.route("/first_form",methods = ["Get","post"])
# first page
def first_form():
    try:
        if(request.method == "POST"):
            button_clicked = request.form['button_clicked']
            print("hi")
            if button_clicked == 'button1':
                # Processing for the first button click
                return render_template("User/login_user.html")
            if button_clicked == 'button2':
                # Processing for the second button click
                return render_template("/owner/owner_login.html")
    except Exception as e:
        return f"Error :{e}!\nPlease Contact Developers"
    return "INVALID REQUEST"

def validate_user_credentials(us_id,password):
    val = store.read_pickle_file(store.users_file)
    for i in val:
        if(i.id == us_id and i.password == password):
            return True

  
# Signin page
@app.route("/signin_form", methods=['POST', 'GET'])
def signin_form():
    try:
        if request.method == "POST":
            users_id = request.form['userid']
            password = request.form['pass']
            button_clicked = request.form['button_clicked']

            # Assume you have a function to validate user credentials
            if validate_user_credentials(users_id, password):
                if button_clicked == 'btn1':
                    f1 = open("C:/Users/user/OneDrive/Documents/PDP project/data.txt",'w')
                    f1.write(users_id)
                    return render_template("User/direct.html")
            else:
                error_message = "Invalid User ID or Password"
                return render_template("User/login_user.html", error_message=error_message)

    except Exception as e:
        return f"Error: {e}!\nPlease Contact Developers"

    return "INVALID REQUEST"



@app.route("/get_signup_page")
def get_signup_page():
    return render_template("/User/signup.html")


#Signup page
@app.route("/signup_form", methods=['POST', 'GET'])
def signup_form():
    global store
    try:
        if(request.method == "POST"):
            button_clicked = request.form['button_clicked']
            if button_clicked == 'btn1':
                u_id = request.form['id']
                u_name = request.form['user_name']
                password = request.form['password']
                email = request.form['email']
                phone = request.form['phone_number']
                u1 = user(u_id,u_name,password,email,phone)
                # Storing values through a single object
                print(u1.count)
                store.store_user(u1)
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
                print(store.users_file)
                f1 = open("C:/Users/user/OneDrive/Documents/PDP project/data.txt",'r')
                users_id = f1.read()
                print(users_id)
                val = store.read_pickle_file(store.users_file)
                display = []
                for i in val:
                    print(i.id,users_id)
                    if(i.id == users_id):
                        
                        for i in i.orders:
                            op = []
                            op.append(i.id)
                            op.append(i.t_type)
                            op.append(i.tb_no)
                            op.append(i.date)
                            op.append(i.timing)
                            display.append(op)
                return render_template("/User/order_log.html",results = display)
    except Exception as e:
        return f"Error :{e}!\nPlease Contact Developers"
    return "INVALID REQUEST"


#Booking
@app.route("/book_form", methods=['POST', 'GET'])
def book_form():
    global us_id, table_no, timing, date, t_type,users_id
    try:
        if request.method == "POST":
            button_clicked = request.form['button_clicked']
            us_id = request.form['id']
            table_no = request.form['table_no']
            timing = request.form['timings']
            date = request.form['date']
            t_type = request.form['types']
            if(len(table_no) == 1):
                val = [table_no]
            else:
                val = table_no.split(",")
            if button_clicked == 'btn1':
                # Facade user's interface method
                print(us_id,val)
                cal_dis = f.cal_price(t_type,val,us_id)
                print(cal_dis)
                if(cal_dis[1] == 0):
                    table = [us_id, t_type, table_no, timing, date, cal_dis[0], cal_dis[1], cal_dis[0]]
                    return render_template("/User/payment.html", results=table)

                table = [us_id, t_type, table_no, timing, date, cal_dis[0], cal_dis[1], cal_dis[2]]

                return render_template("/User/payment.html", results=table)

    except Exception as e:
        return f"Error: {e}!\nPlease Contact Developers"

    return "INVALID REQUEST"

@app.route('/get_data')
def get_data():
    try:
        with open('C:/Users/user/OneDrive/Documents/PDP project/date.json', 'r') as file:
            data = json.load(file)
        return jsonify(data)
    except Exception as e:
        print(f"Error loading JSON data: {e}")
        return jsonify([])
        
@app.route("/direct_page",methods = ["Get","post"])
# first page
def direct_page():
    global us_id,table_no,timing,t_type,date,f
    try:
        if(request.method == "POST"):
            button_clicked = request.form['button_clicked']
            if button_clicked == 'btn1':
                print(date)
                O1 = Orders(us_id,table_no,timing,t_type,date)
                b = Book()
                b.upd_orders(O1)
                print("user_updated")
                b.up_owners(O1)
                print("owner_updated")
                print(type(table_no))
                tb_no = table_no.split(",")
                f.change_state(tb_no,timing,t_type,date)
                return render_template("User/final.html")

    except Exception as e:
        return f"Error :{e}!\nPlease Contact Developers"
    return "INVALID REQUEST"  

@app.route("/pm_comp",methods = ["Get","post"])
# first page
def pm_comp():
    try:
        if(request.method == "POST"):
            button_clicked = request.form['button_clicked']
            print("hi")
            if button_clicked == 'btn1':
                # Processing for the first button click
                return render_template("User/direct.html")
    except Exception as e:
        return f"Error :{e}!\nPlease Contact Developers"
    return "INVALID REQUEST"  

@app.route("/ord_log",methods = ["Get","post"])
def ord_log():
    return "Submited"
            
#Owner Module

def validate_owner_credentials(us_id,password):
    val = store.read_pickle_file(store.owner_file)
    print(val)
    for i in val:
        print(i.id,i.password)
        if(i.id == us_id and i.password == password):
            return True

@app.route("/ow_signin_form",methods = ['GET','POST'])
def ow_signin_form():
    global owners_id
    try:
        if request.method == "POST":
            owner_id = request.form['userid']
            password = request.form['pass']
            button_clicked = request.form['button_clicked']
            print("shown")
            # Assume you have a function to validate user credentials
            if validate_owner_credentials(owner_id, password):
                print(True)
                owners_id = owner_id
                print(users_id)
                if button_clicked == 'btn1':
                    # return render_template("User/direct.html")
                    return render_template("owner/owner_direct.html")
            else:
                print(False)
                error_message = "Invalid User ID or Password"
                return render_template("owner/owner_login.html", error_message=error_message)

    except Exception as e:
        return f"Error: {e}!\nPlease Contact Developers"

    return "INVALID REQUEST"

@app.route("/ow_get_signup_page")
def ow_get_signup_page():
    return render_template("owner/owner_signup.html")

@app.route("/ow_signup_form",methods = ['POST','GET'])
def ow_signup_form():
    global store
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
                o1 = owner(u_id,u_name,password,email,phone)
                # Storing values through a single object
                store.store_owner(o1)
                return render_template("/owner/owner_login.html")
            if button_clicked == 'btn2':
                # Processing for the second button click
                return render_template("/owner/owner_login.html")
    except Exception as e:
        return f"Error :{e}!\nPlease Contact Developers"
    return "INVALID REQUEST"


@app.route("/ow_direct_form",methods = ['POST','GET'])
def ow_direct_form():
    try:
        if(request.method == "POST"):
            button_clicked = request.form['button_clicked']
            if button_clicked == 'btn1':
                print(store.users_file)
                val = store.read_pickle_file(store.owner_file)
                display = []
                print(val)
                for i in val:
                    for i in i.orders:
                        op = []
                        op.append(i.id)
                        op.append(i.t_type)
                        op.append(i.tb_no)
                        op.append(i.date)
                        op.append(i.timing)
                        print(op)
                        display.append(op)
                return render_template("/owner/owner_log.html",results = display)
    except Exception as e:
        return f"Error :{e}!\nPlease Contact Developers"
    return "INVALID REQUEST"

if __name__ == "__main__":
    app.run(debug = True)