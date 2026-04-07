from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    nombre = "Zacarias Flores Perez"
    edad=22
    return render_template("index.html", nombre=nombre, edad=edad)

if __name__ =='__main__':
    app.run(debug=True)