from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def bienvenida():
    return render_template('index.html', mensaje="¡Bienvenido a mi aplicación web!")

@app.route('/api/mensaje')
def obtener_mensaje():
    return {'mensaje': '¡Hola Inge 🤯!'}

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
