from typing import final
import pymysql 

class DAOProducto:

    def __init__(self):
        pass

    def connect():
        return pymysql.connect(host='localhost',
                               user='root',
                               password='humbertobernal',
                               database='proyecto_db')

    def read(self,id=None):
        con = DAOProducto.connect()
        cursor = con.cursor()

        try:
            if id==None:
               cursor.execute("SELECT * FROM producto order by codigo")
            else:
               cursor.execute("SELECT * FROM producto where id = %s",(id,))
            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()

        
    def insert(self,data=None):
        con = DAOProducto.connect()
        cursor = con.cursor()

        codigo = data['codigo']
        descripcion = data['descripcion']
        precio = data['precio']
        stock = data['stock']
        categoria = data['categoria']
        
        try:
            cursor.execute("INSERT INTO producto(codigo,descripcion,precio,stock,categoria) VALUES(%s,%s,%s,%s,%s)",(codigo,descripcion,precio,stock,categoria))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()


    def update(self,id,data): 
        con = DAOProducto.connect()
        cursor = con.cursor()
        
        c = data['codigo']
        d = data['descripcion']
        p = data['precio']
        s = data['stock']
        ca = data['categoria']

        try:
           cursor.execute("UPDATE producto SET codigo=%s, descripcion=%s, precio=%s, stock=%s, categoria=%s WHERE id=%s ",(c,d,p,s,ca,id))
           con.commit()
           return True
        except:
           con.rollback()
           return False
        finally:
           con.close()

    def delete(self,id):
        con = DAOProducto.connect()
        cursor = con.cursor()
        
        try:
            cursor.execute("DELETE FROM producto WHERE id=%s ",(id,))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()
