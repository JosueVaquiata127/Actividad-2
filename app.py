from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        telefono = request.form['telefono']

        return render_template('registro.html',  mensaje="¡Registro exitoso!",  nombre=nombre, email=email, telefono=telefono )

    return render_template('registro.html')

if __name__ == '__main__':
    app.run(debug=True)