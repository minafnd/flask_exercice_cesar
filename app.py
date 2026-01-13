from cesar import cesar, decesar
from flask import Flask, request, render_template, redirect, flash

app = Flask(__name__) 
app.secret_key = "supersecretkey"

@app.route("/")
def home():
    return "Bienvenue dans l'application de (dé)chiffrement César ! "

@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        # Traitement des données
       
        msg = request.form.get("message", "").strip()
        crypttype = request.form.get("crypttype", "")
        shift = request.form.get("shift", "").strip()

        errors = []

        if not msg:
            errors.append("Message is required.")
        if not shift or not shift.isdigit():
            errors.append("Shift is required and must be a number")
        if errors:
            for error in errors:
                flash(error, "error")
            return redirect("/form")


        if crypttype == "chiffrement":
            result = cesar(msg, int(shift))
        
            
        else:
            result = decesar(msg, int(shift))
        return render_template('form.html', result=result, msg=msg, crypttype=crypttype, shift=shift)
        
    
    return render_template("form.html")



if __name__ == "__main__":
    app.run(debug=True)