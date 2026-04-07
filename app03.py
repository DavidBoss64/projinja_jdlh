from flask import Flask, render_template, request, url_for,redirect
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():
    #Verificar si el usuario esta logueado
    if request.method == 'POST':
        nombre = request.form['usuario']
        password = request.form['password']
        #Aqui
        return redirect(url_for('user',user=nombre))
        #Si no esta logueado, mostrar el formulario de login
    else:
        return render_template('login.html')


@app.route('/<user>')
def user(user):
    return f'<h1> Hola {user}</h1>'
if __name__ == '__main__':
    app.run(debug=True)