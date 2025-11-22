from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")
    
    # (Optional) Save message to database or send email
    print("New Contact Message:")
    print("Name:", name)
    print("Email:", email)
    print("Message:", message)

    return render_template("success.html", name=name)

if __name__ == "__main__":
    app.run(debug=True)
