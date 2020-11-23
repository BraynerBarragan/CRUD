from flask import Flask, render_template, request, redirect, url_for
import sqlite3
db=sqlite3.connect('data.db', check_same_thread=False)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

#@app.route('/contacto', methods=['GET', 'POST'])
#def contacto():
#    # obtener formulario
#    if request.method=='GET':
#        return render_template('contactos.html')
#    # guardando la informacion
#    nombre= request.form.get('nombres')
#    return 'Guardando informacion...' + nombre

@app.route('/usuarios')
def usuarios():
    usuarios= db.execute('select * from usuarios').fetchall()
    #usuarios= usuarios.fetchall()  
    return render_template('usuarios/listar.html', usuarios=usuarios)


@app.route('/usuarios/crear', methods=('GET', 'POST'))
def crear_usuarios():
    if request.method == 'GET':
        return render_template('usuarios/crear.html')

    nombres = request.form.get('nombres')    
    apellidos = request.form.get('apellidos')    
    email = request.form.get('email')    
    password = request.form.get('password')

    cursor=db.cursor()
    cursor.execute(""" insert into usuarios(
        nombres,
        apellidos,
        email,
        password
    )values(?,?,?,?)
    """,(nombres, apellidos, email, password)) 
    db.commit()
    return redirect(url_for('usuarios'))
# ------  EDITAR  --------
@app.route('/usuarios/editar/<id>',)
def editar(id):
    act=db.execute('select * from usuarios where id=?',(id,)).fetchone()
    if request.method == 'GET':
        return render_template('usuarios/actualizar.html',fila=act)

@app.route('/usuarios/<id>', methods=('GET', 'POST'))
def guardar_cambios(id):

    nombres = request.form.get('nombres')    
    apellidos = request.form.get('apellidos')    
    email = request.form.get('email')    
    password = request.form.get('password')

    cursor=db.cursor()
    cursor.execute(' UPDATE usuarios SET nombres = ?, apellidos = ?, email = ?,password = ? WHERE id = ?',(nombres, apellidos, email, password, id)) 
    db.commit()

    return redirect(url_for('usuarios'))

# ------ ELIMINAR ------
@app.route('/usuarios/eliminar/<id>')
def eliminar(id):
    cursor=db.cursor()
    cursor.execute('delete from usuarios where id=?',(id,))
    db.commit()
    return redirect(url_for('usuarios'))

@app.route('/usuarios/eliminar_todo')
def eliminar_todo():
    cursor=db.cursor()
    cursor.execute('delete from usuarios')
    db.commit()
    return redirect(url_for('usuarios'))
    
    


    
 


app.run(debug=True)    