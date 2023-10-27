from datetime import timedelta
import hashlib
from itertools import product
from random import randint
from flask import Flask,render_template,request,redirect, send_from_directory,session
import mysql.connector
from productos import Productos
import os

app= Flask(__name__)
conexion= mysql.connector.connect(
    host="127.0.0.1",
    database="inventario",
    port="3306",
    user='root',
    password=''
    )

miCursor=conexion.cursor()
productosI=Productos(app,conexion,miCursor)

@app.route("/recargar")
def recargar():
    sql=f"SELECT * FROM insumos"
    miCursor.execute(sql)
    resultado=miCursor.fetchall()
    conexion.commit()
    return render_template("productos.html",res=resultado)

    

@app.route("/")
def productos():
    sql=f"SELECT * FROM insumos"
    miCursor.execute(sql)
    resultado=miCursor.fetchall()
    conexion.commit
    return render_template("productos.html",res=resultado)


@app.route("/agregarproducto")
def agregarproducto():
    return render_template("agregarproducto.html")


@app.route("/guardar", methods=["POST"])
def guardarproducto():
    sql="SELECT * FROM insumos"
    miCursor.execute(sql)
    resultado = miCursor.fetchall()
    conexion.commit()
    prod=request.form["prod"]
    desc=request.form["desc"]
    cant=request.form["cant"]
    categ=request.form["categ"]
    producto=[prod,desc,cant,categ]
    productosI.agregarproducto(producto)
    return redirect("/recargar")

@app.route("/actualizar", methods=['POST'])
def actualizaproducto():
    prod=request.form["prod"]
    desc=request.form["desc"]
    cant=request.form["cant"]
    categ=request.form["categ"]
    producto=[prod,desc,cant,categ]
    productosI.actualiza(producto)
    return redirect("/recargar")

if __name__=='__main__':
    app.run(host="0.0.0.0",debug=True,port="8090")