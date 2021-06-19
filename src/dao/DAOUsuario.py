from typing import final
import pymysql 

class DAOUsuario:

    def __init__(self):
        pass

    def connect():
        return pymysql.connect(host='localhost',
                               user='root',
                               password='humbertobernal',
                               database='proyecto_db')

    def read(self,id=None):
        con = DAOUsuario.connect()
        cursor = con.cursor()

        try:
            if id==None:
               cursor.execute("SELECT * FROM usuario order by nombre")
            else:
               cursor.execute("SELECT * FROM usuario where id = %s",(id,))
            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()

        
    def insert(self,data=None):
        con = DAOUsuario.connect()
        cursor = con.cursor()

        nombre = data['nombre']
        telefono = data['telefono']
        email = data['email']
        

        try:
            cursor.execute("INSERT INTO usuario(nombre,telefono,email) VALUES(%s,%s,%s)",(nombre,telefono,email,))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()


    def update(self,id,data): 
        con = DAOUsuario.connect()
        cursor = con.cursor()
        
        nombre = data['nombre']
        telefono = data['telefono']
        email = data['email']
        try:
           cursor.execute("UPDATE usuario SET nombre=%s,telefono=%s,email=%s WHERE id=%s ",(nombre,telefono,email,id,))
           con.commit()
           return True
        except:
           con.rollback()
           return False
        finally:
           con.close()

    def delete(self,id):
        con = DAOUsuario.connect()
        cursor = con.cursor()
        
        try:
            cursor.execute("DELETE FROM usuario WHERE id=%s ",(id,))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()
