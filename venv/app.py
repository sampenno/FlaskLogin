from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

#dummy user name and password
USERNAME = "admin"
PASSWORD = "password"

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Get the form data
        username = request.form.get("username")
        password = request.form.get("password")

        # Check user credentials
        if username == USERNAME and password == PASSWORD:
            return redirect(url_for("welcome"))
        else:
            return render_template("login.html", error=" invalid username or password")
    return render_template("login.html")
@app.route("/welcome")

def welcome():
    return render_template("welcome.html")

if __name__ == "__main__":
    app.run(debug=True)