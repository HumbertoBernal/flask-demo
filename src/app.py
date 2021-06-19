import re
from flask import Flask, flash, render_template, redirect, sessions, url_for, request, session
from dao.DAOUsuario import DAOUsuario
from dao.DAOProducto import DAOProducto

app = Flask(__name__)
app.secret_key = 'Utec123'
db = DAOUsuario()
dbProducto = DAOProducto()

@app.route('/')
def inicio():
    return render_template("index.html")

@app.route('/usuario/')
def inicioUsuario():
    return render_template("usuario/index.html", usuarios=db.read(None))

@app.route('/usuario/add/', methods=['POST','GET'])
def agregarUsuario():
    if request.method == 'POST' and request.form['save']:
        nombre = request.form['nombre']
        telefono = request.form['telefono']
        email = request.form['email']
        data = {
          'nombre': nombre,
          'telefono': telefono,
          'email': email
        }
        db.insert(data)
        return redirect(url_for('inicioUsuario'))
    elif request.method == 'GET':
        return render_template("usuario/add.html")

@app.route('/usuario/update/<int:id>', methods=['POST','GET'])
def usuario_update(id):
    if request.method == 'POST' and request.form['save']:
        nombre = request.form['nombre']
        telefono = request.form['telefono']
        email = request.form['email']
        data = {
          'nombre': nombre,
          'telefono': telefono,
          'email': email
        }
        db.update(session['update'], data)
        session.pop('update', None)
        return redirect(url_for('inicioUsuario'))
        
    elif request.method == 'GET':
        usuario=db.read(id)
        if usuario:
            usuario = usuario[0]
            session['update'] = id 
            return render_template('usuario/update.html', u=usuario)  
        else:
            return redirect(url_for('inicioUsuario'))    

@app.route('/usuario/delete/<int:id>', methods=['POST','GET'])
def usuario_delete(id):
    if request.method == 'POST' and request.form['save']:
        n = session['delete']
        if db.delete(n):
            session.pop('delete', None)
            return redirect(url_for('inicioUsuario'))
    elif request.method == 'GET':
        usuario=db.read(id)
        if usuario:
            usuario = usuario[0]
            session['delete'] = id 
            return render_template('usuario/delete.html', u=usuario)   
        else:
            return redirect(url_for('inicioUsuario'))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html')

@app.route('/empleado/')
def inicioEmpleado():
    return render_template("empleado/index.html")

@app.route('/producto/')
def inicioProductos():
    return render_template("producto/index.html", productos=dbProducto.read(None))

@app.route('/producto/add/', methods=['POST','GET'])
def producto_add():
    if request.method == 'POST' and request.form['save']:
        dbProducto.insert(request.form)
        return redirect(url_for('inicioProductos'))
    elif request.method == 'GET':
        return render_template("producto/add.html")

@app.route('/producto/update/<int:id>', methods=['POST','GET'])
def producto_update(id):
    if request.method == 'POST' and request.form['save']:
        dbProducto.update(session['update'], request.form)
        session.pop('update', None)
        return redirect(url_for('inicioProductos'))
        
    elif request.method == 'GET':
        producto=dbProducto.read(id)
        if producto:
            producto = producto[0]
            session['update'] = id 
            return render_template('producto/update.html', u=producto)  
        else:
            return redirect(url_for('inicioProductos'))    

@app.route('/producto/delete/<int:id>', methods=['POST','GET'])
def producto_delete(id):
    if request.method == 'POST' and request.form['save']:
        n = session['delete']
        if dbProducto.delete(n):
            session.pop('delete', None)
            return redirect(url_for('inicioProductos'))
    elif request.method == 'GET':
        producto=dbProducto.read(id)
        if producto:
            producto = producto[0]
            session['delete'] = id 
            return render_template('producto/delete.html', u=producto)   
        else:
            return redirect(url_for('inicioProductos'))

@app.route('/login')
def login():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True, port=3000,host="0.0.0.0")
