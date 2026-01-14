from cesar import cesar, decesar
from flask import Flask, request, render_template, redirect, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) 
app.secret_key = "supersecretkey"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class HistoryEntry(db.Model):
    __tablename__ = 'history'

    id = db.Column(db.Integer, primary_key=True)
    action = db.Column(db.String(10), nullable=False)
    message = db.Column(db.Text, nullable=False)
    key = db.Column(db.Integer, nullable=False)
    result = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return f"HistoryEntry('{self.action}', '{self.message}', '{self.key}', '{self.result}', '{self.created_at}')"
    
# création de la table dans SQLite
with app.app_context(): #le même with qu'on utilise pour le traitement de fichiers (json, csv)
    db.create_all()

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

        entry = HistoryEntry(message=msg, action=crypttype, key=shift, result=result)
        db.session.add(entry)
        db.session.commit()


        return render_template('form.html', result=result, msg=msg, crypttype=crypttype, shift=shift)
        
    
    return render_template("form.html")


@app.route("/history")
def history():
    entries = HistoryEntry.query.all()
    return render_template("history.html", entries=entries)


if __name__ == "__main__":
    app.run(debug=True)