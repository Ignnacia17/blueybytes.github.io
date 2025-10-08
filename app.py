from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", section="hamsters")

@app.route("/hamsters")
def hamsters():
    return render_template("index.html", section="hamsters")

@app.route("/ratas")
def ratas():
    return render_template("index.html", section="ratas")

@app.route("/erizos")
def erizos():
    return render_template("index.html", section="erizos")

@app.route("/blog")
def blog():
    return render_template("index.html", section="blog")

@app.route("/contacto")
def contacto():
    return render_template("index.html", section="contacto")

if __name__ == "__main__":
    app.run(debug=True)
