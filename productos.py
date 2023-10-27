from datetime import datetime
from flask import render_template,redirect
import os
import mysql.connector
conexion = mysql.connector.connect(
    host="127.0.0.1",
    database="articulos",
    port="3306",
    user='root',
    password=''
)


class Productos:
    def __init__(self,app,db,cursor):
        self.app=app
        self.db=db
        self.cursor=cursor


    def buscar(self):
        sql=f"SELECT * FROM insumos"
        self.cursor.execute(sql)
        resultado=self.cursor.fetchall()
        conexion.commit()
        return resultado
    
    def agregarproducto(self, prod):
        sql = f"INSERT INTO insumos (Producto, Descripcion, Cantidad, Categoria) VALUES ('{prod[0]}', '{prod[1]}', '{prod[2]}', '{prod[3]}')"
        self.cursor.execute(sql)
        self.db.commit()


    def consultar(self):
        sql= "SELECT * FROM insumos"
        self.cursor.execute(sql)
        resultado=self.cursor.fetchall()
        return resultado

    def actualiza(self,prod):
        sql =f"INSERT INTO insumos (Producto,Descripcion,Cantidad,Categoria) VALUES ('{prod[0]}','{prod[1]}','{prod[2]}','{prod[3]}')" 
        self.cursor.execute(sql)
        self.cursor.execute(sql)
        self.db.commit()


    def borrar(self,prod):
        sql=f"DELETE from insumos WHERE Producto = '{prod}'"
        self.cursor.execute(sql)
        self.db.commit()