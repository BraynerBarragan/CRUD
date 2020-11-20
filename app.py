from flask import Flask, render_template, request
import sqlite3
db=sqlite3.connect('data.db', check_same_thread=False)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    # obtener formulario
    if request.method=='GET':
        return render_template('contactos.html')
    # guardando la informacion
    nombre= request.form.get('nombres')
    return 'Guardando informacion...' + nombre

@app.route('/usuarios')
def usuarios():
    usuarios= db.execute('select * from usuarios').fetchall()
    #usuarios= usuarios.fetchall()  
    return render_template('usuarios/listar.html', usuarios=usuarios)


@app.route('/usuarios/crear', methods=('GET', 'POST'))
def crear_usuarios():

    return render_template('usuarios/crear.html')

app.run(debug=True)    