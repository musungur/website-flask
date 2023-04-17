'''This is a new file to execute a task as a python script.'''
from flask import Flask, render_template, redirect, request, url_for
import csv
import os
import time
import sqlite3
import pymongo

time = time.asctime()

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("beta-registerform.html")

@app.route("/register", methods=["POST"])
def registered():
#    name = request.form.get("name")
#    email = request.form.get("email")
    formtype = request.form.get("formtype")
    if formtype != "":
#        return render_template("success.html")
        if formtype == "Leave out form":
            return render_template("./forms/leave-out-form.html")
#            return "Leave out form"
        elif formtype == "Gate pass":
#            return "Gate pass"
            return render_template("./forms/Gate-pass.html")
        elif formtype == "Leav Book":
            return "Leav Book"
#            return render_template("Leav-Book.html")
        elif formtype == "Inventory Movement":
            return "Inventory Movement"
#            return render_template("Inventory-Movement.html")
        elif formtype == "Cheque Requisition":
            return "Cheque Requisition"
#            return render_teemplate("Cheque-Reguisition.html")
        elif formtype == "sales Report":
            return "Sales Report"
#            return render_template("Sales-Report.html")

    return render_template("failure.html")

@app.route("/leave-out-form", methods=["POST"])
def leaveout():
    fname = request.form.get("fname")
    sname = request.form.get("sname")
    deptm = request.form.get("dptm")
    empno = request.form.get("empno")
    telno = request.form.get("telno")
    stime = request.form.get("stime")
    etime = request.form.get("etime")
    msg = request.form.get("reason")
    date = request.form.get("date")

    if fname != "" and sname != "" and date != "" and deptm != "" and telno != "" and msg != "" and empno !="" and stime != "" and etime != "" and stime < etime:
        #'import leaveout-write'write below as separate pyfile and import here. keeps code clean.also reason is, this code is repetetive
        with open("betacare-backup.csv","a") as fo:
            writer = csv.writer(fo)
            writer.writerow((request.form.get("fname"),request.form.get("sname"),request.form.get("deptm"),request.form.get("empno"),request.form.get("telno"),request.form.get("stime"),request.form.get("etime"),request.form.get("msg"),request.form.get("date")))
            fo.write(f"{fname} submitted on {time}\n")
 #after writing to backup,returns success! user tosee success message.Redirect back to("/").user waite at gate, gateman needs to see diss/approved/
        return render_template("success.html")
#
    return render_template("failure.html")

@app.route("/approvals")
def confirm():
    with open("betacare-backup.csv","r") as fi:
        forms = fi.readlines()
        return render_template("./forms/approvals.html",forms=forms)

@app.route("/gatepass", methods=["POST"])
def gatepass():
    lab1 = request.form.get("l1")
    lab2 = request.form.get("l2")
    lab3 = request.form.get("l3")
    lab4 = request.form.get("l4")
    name = request.form.get("name")
    num = request.form.get("nplate")
    timer = request.form.get("timer")
    msg = request.form.get("textarea")
    if name !="" and num !="" and timer !="" and msg != "":
        with open("gatepass.csv","a") as fo:
            writer = csv.writer(fo)
            writer.writerow((request.form.get("name"),request.form.get("nplate"),request.form.get("timer"),request.form.get("textarea")))
            fo.write("\n")
            return render_template("success.html")
    else:
        return render_template("failure.html")
#    return render_template("./forms/Gate-pass.html")

#success button redirect to home page
@app.route("/button", methods=["POST"])
def button():
    return redirect(url_for("homepage"))

#General failure:redirect to homepage
@app.route("/try", methods=["POST"])
def failure():
    return redirect(url_for("homepage"))

#leave-out-form trial
@app.route("/leave-out", methods=["POST"])
def leaveoutform():
    return render_template("./forms/leave-out-form.html")

#Gatepass trial
@app.route("/gatep", methods=["POST"])
def gatepasstrial():
    return render_template("./forms/Gate-pass.html")


'''
#LeavBook trial
@app.route("/lbook", methods=["POST"])
def leavbooktrial():
    return render_template("")

#inventoryMovement trial
@app.route("/inventmvmnt", methods=["POST"])
def inventory():
    return render_template("")

#SalesRepport trial
@app.route("/salesreport", methods=["POST"])
def SalesReport():
    return render_template("")

#Cheque Requisition trisl
@app.route("/cheque", methods=["POST"])
def cheque():
    return render_template("")
'''

#Cancel
@app.route("/cancel", methods=["POST"])
def cancel():
    return redirect(url_for("homepage"))


@app.route("/sql", methods=["POST"])
def Tosqldb():
    name = request.form.get("name")
    nplate = request.form.get("nplate")
    timer = request.form.get("timer")
    message = request.form.get("textarea")

#    data =[({name},{message})]


    path = os.getcwd()
    conn = sqlite3.connect("DATABASE.db")
    
    c = conn.cursor()
    query1 = "INSERT INTO gatepass VALUES ('{n}','{pl}','{timer}','{m}')".format(n = name, pl = nplate, m = message)
    c.execute(query1)
    conn.commit()
    conn.close()
    return render_template("success.html")
#have commented tablecreation since have already created it/run the script
'''
    c.execute("""CREATE TABLE GgatePass2 (
    Name text,
    Message text
    )""")
'''
'''
    c.executemany("INSERT INTO GGgatteBack VALUES (?,?)",data)
   # c.execute("")
    conn.commit()
    conn.close()
    return render_template("success.html")
'''
#    query1 = "INSERT INTO gatepass VALUES ('{n}','{pl}','{m}')".format(n = name, pl = nplate, m = message)
'''
    c.execute(query1)

    
    conn.commit()
    conn.close()                                      return render_template("success.html")
'''

# mongodb connections
@app.route("/mongo", methods=["POST"])
def database():
    try:
        mongo = pymongo.MongoClinet(
                host = localhost,
                port = 27017,
                serverSelectionTimeoutMS = 1000,
                )
        db = mongo.company
        print(db.status_code)


        mongo.server_info() #triggers to capture the exceptions
    except:
        print("Cannot connect to mongodb")


if __name__ == "__main__":
    app.run(debug=True)
