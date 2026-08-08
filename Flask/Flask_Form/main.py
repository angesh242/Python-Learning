from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/", methods=["GET","POST"])
def hello_world():
   if (request.method == "POST"):
       #Handlethe form
       with open("data.txt", "a") as f:
           f.write(f"{request.form['name']}, {request.form['email']}, {request.form['message']}\n")
       
       return render_template("contact.html")
   else:
    return render_template("contact.html")


app.run(debug=True)