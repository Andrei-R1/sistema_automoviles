from flask import Flask, json, jsonify,request
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()
# url del servidor de MySQL
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
# nombre de usuario
app.config['MYSQL_DATABASE_USER'] = 'root'
# contrasena
app.config['MYSQL_DATABASE_PASSWORD'] = ''
# nombre de base de datos
app.config['MYSQL_DATABASE_DB'] = 'sistema_empresa_automoviles'
mysql.init_app(app)

@app.route("/")
def index_route():
    return "Bienvenido al sistema de la concesionaria de automoviles"

@app.route('/clientes', methods={'GET','POST'})
def index_clientes():
    if (request.method == 'POST'):
        registro_clientes = request.get_json();
        print(registro_clientes)

        clientes_cedula = registro_clientes['clientes_cedula']
        clientes_tipo_cedula = registro_clientes['clientes_tipo_cedula']
        clientes_nombre = registro_clientes['clientes_nombre']
        clientes_apellido = registro_clientes['clientes_apellido']
        clientes_calificacion_credito = registro_clientes['clientes_calificacion_credito']
        clientes_direccion= registro_clientes['clientes_direccion']
        clientes_telefono = registro_clientes['clientes_telefono']
        clientes_fecha_nacimiento = registro_clientes['clientes_fecha_nacimiento']

        conn = mysql.connect()
        cur = conn.cursor()

        cur.execute("INSERT INTO clientes(clientes_cedula,clientes_tipo_cedula,clientes_nombre,clientes_apellido,clientes_calificacion_credito,clientes_direccion,clientes_telefono,clientes_fecha_nacimiento)VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",(clientes_cedula,clientes_tipo_cedula,clientes_nombre,clientes_apellido,clientes_calificacion_credito,clientes_direccion,clientes_telefono,clientes_fecha_nacimiento))
        conn.commit()
        cur.close()
        return jsonify({"Response" : "¡Cliente Agregado con Exito!"}),200

    else:
        conn = mysql.connect()
        cur = conn.cursor()
        cur.execute("SELECT * FROM clientes")
        datos_clientes = cur.fetchall()
        respuesta = [] 
        for clientes in datos_clientes:
            respuesta.append({        
        "Cedula clientes ": clientes[0],
        "Tipo de cedula ": clientes [1] ,
        "Nombre y Apellido ":  (clientes)[2] +" "+ (clientes) [3],
        "Calificacion de credito ": clientes[4],
        "Direccion ": clientes[5],
        "Telefono ": clientes[6],
        "Fecha De Nacimiento ": clientes[7],
        }) 
        cur.execute("SELECT * FROM vendedores")
        datos_vendedores = cur.fetchall()
        respuesta1 = []
        for vendedores in datos_vendedores:
            respuesta1.append({
        "CIV ": vendedores[0],
        "Nombre y Apellido ": vendedores[1] + ' '+ vendedores[2],
        "Numero de Telefono ": vendedores[7]})
        cur.execute("SELECT * FROM ventas")
        datos_ventas = cur.fetchall()
        respuesta2 = []
        for ventas in datos_ventas:
            respuesta2.append({
            "CIV ": ventas[0],
            "Codigo Consecutivo ": ventas[1],
            "Monto ": ventas[5],
            "Fecha de venta ": ventas[6],
            "Tipo de Automovil ": ventas[8] + ", " + ventas[9] + ", " + ventas[10]
        })
        return jsonify ({"Cliente": respuesta, "Vendedores Info": respuesta1, "Ventas Registro": respuesta2}),200

    


@app.route('/vendedores', methods ={'POST', 'GET'})
def index_vendedores():
    if (request.method == 'POST'):
        registro_vendedores = request.get_json();
        print(registro_vendedores)
        vendedores_civ = registro_vendedores['vendedores_civ']
        vendedores_nombre = registro_vendedores['vendedores_nombre']
        vendedores_apellido = registro_vendedores['vendedores_apellido']
        vendedores_fecha_nacimiento = registro_vendedores['vendedores_fecha_nacimiento']
        vendedores_tipo = registro_vendedores['vendedores_tipo']
        vendedores_salario= registro_vendedores['vendedores_salario']
        vendedores_direccion = registro_vendedores['vendedores_direccion']
        vendedores_telefono = registro_vendedores['vendedores_telefono']
        vendedores_porcentaje_comision = registro_vendedores['vendedores_porcentaje_comision']
        vendedores_monto_comision = registro_vendedores['vendedores_monto_comision']

        
        conn = mysql.connect()
        cur = conn.cursor()

        cur.execute("INSERT INTO vendedores(vendedores_civ,vendedores_nombre,vendedores_apellido,vendedores_fecha__comisionnacimiento,vendedores_tipo,vendedores_salario,vendedores_direccion,vendedores_telefono,vendedores_porcentaje_comision,vendedores_monto_comision)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(vendedores_civ,vendedores_nombre,vendedores_apellido,vendedores_fecha_nacimiento,vendedores_tipo,vendedores_salario,vendedores_direccion,vendedores_telefono,vendedores_porcentaje_comision,vendedores_monto_comision))
        conn.commit()
        cur.close()
        return jsonify({"Response" : "¡Vendedor Agregado con Exito!"}),201

    else:
        conn = mysql.connect()
        cur = conn.cursor()
        cur.execute("SELECT * FROM vendedores")
   

        datos_vendedores = cur.fetchall()
        respuesta = []
        for vendedores in datos_vendedores:
            respuesta.append(
        {
         "Vendedor CIV ": vendedores[0],
         "Vendedor Nombre y Apellido": vendedores[1] + ' '+ vendedores[2],
         "Fecha de nacimiento ": vendedores [3],
         "Tipo de vevendedoresndedor ": vendedores[4],
         "Salario ": vendedores[5],
         "Direccion ": vendedores[6],
         "Numero de contacto ": vendedores[7],
         "Porcentaje ": vendedores[8],
         "Monto " : vendedores[9],

        }) 
        cur.execute("SELECT * FROM clientes")
        datos_clientes = cur.fetchall()
        respuesta1 = []
        for clientes in datos_clientes:
         respuesta1.append({
             "Cedula ": clientes[0],
             "Nombre y Apellido": clientes[2] + ' ' + clientes[3],
             "Numero de Telefono ": clientes[6]})
        return jsonify ({"Almacenaje Vendedores": respuesta, "Clientes": respuesta1}),200
    
@app.route('/ventas', methods={'POST','GET'})
def index_ventas():
    if (request.method == 'POST'):
        nueva_venta = request.get_json();
        print(nueva_venta)
        venta_cuv = nueva_venta['venta_cuv']
        venta_codigo_consecutivo = nueva_venta['venta_codigo_consecutivo']
        venta_contrato = nueva_venta['venta_contrato']
        venta_civ = nueva_venta['venta_civ']
        venta_cedula = nueva_venta['venta_cedula']
        ventas_monto = nueva_venta['venta_monto']
        ventas_fecha = nueva_venta['venta_fecha']
        venta_producto = nueva_venta['venta_producto']
        venta_marca = nueva_venta['venta_marca']
        venta_modelo = nueva_venta['venta_modelo']
        venta_year = nueva_venta['venta_year']
        
        conn = mysql.connect()
        cur = conn.cursor()

        cur.execute("INSERT INTO ventas(venta_cuv,venta_codigo_consecutivo,venta_contrato,venta_civ,venta_cedula,venta_monto,venta_fecha,venta_producto,venta_marca,venta_modelo,venta_year)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",())
        conn.commit()
        cur.close()
        return jsonify({"Response" : "¡Venta Agregada con Exito!"}),201
    else:
        conn = mysql.connect()
        cur = conn.cursor()
        cur.execute("SELECT * FROM ventas")
   
        datos_ventas = cur.fetchall()
        respuesta = []
        for ventas in datos_ventas:
         respuesta.append(
        {
        "CUV ": ventas[0],
        "Codigo de Ventas ": ventas [1] ,
        "Numero de contrato ": ventas [2] , 
        "Vendedores ": ventas [3],
        "Clientes ": ventas[4],
        "Monto ": ventas[5],
        "Fecha de venta ": ventas[6],
        "Producto ": ventas[7],
        "Tipo Automovil: ": ventas[8] + ", " +  (ventas)[9] + ", " +   (ventas)[10],
        })
        cur.execute("SELECT * FROM clientes")
        datos_clientes = cur.fetchall()
        respuesta1 = []
        for clientes in datos_clientes:
            respuesta1.append({
            "Cedula ": clientes[0],
             "Nombre y Apellido ": clientes[2] + ' ' + clientes[3],
             "Numero de Telefono ": clientes[6]})
        cur.execute("SELECT * FROM vendedores")
        datos_vendedores = cur.fetchall()
        respuesta2 = []
        for vendedores in datos_vendedores:
            respuesta2.append({
            "Vendedor CIV": vendedores[0],
            "Nombre Completo": vendedores[1] + " " + vendedores[2],
            "Numero de telefono": vendedores[7],
            "Porcentaje": vendedores[8]
        })
 
    return jsonify ({"Informacion Ventas": respuesta, "Clientes": respuesta1, "Vendedores": respuesta2}),200

@app.route('/clientes/<int:clientes_cedula>')
def clientes_cedula(clientes_cedula):
    conn = mysql.connect()
    cur = conn.cursor()

    cur.execute('SELECT * FROM clientes WHERE clientes_cedula=%s',(clientes_cedula))
    datos_clientes = cur.fetchone()
    
    if datos_clientes == None:
         return jsonify({"response": "No se encontratron registros con ese ID"}),200
    else:
        return jsonify({"response": {
            "Cedula cliente ": datos_clientes[0],
            "Tipo de cedula ": datos_clientes [1] ,
            "Nombre y Apellidos ":  (datos_clientes)[2] +" "+ (datos_clientes) [3],
            "Calificacion del credito ": datos_clientes[4],
            "Direccion ": datos_clientes[5],
            "Telefono ": datos_clientes[6],
            "Fecha De Nacimiento ": datos_clientes[7],
        }}),302

@app.route('/vendedores/<int:vendedores_civ>')
def vendedores_civ(vendedores_civ):
    conn = mysql.connect()
    cur = conn.cursor()

    cur.execute('SELECT * FROM vendedores WHERE vendedores_civ= %s',(vendedores_civ)) 
    datos_vendedores = cur.fetchone()

    if datos_vendedores == None:
        return jsonify({"response":"No se encuentran registros con ese ID "+ str (vendedores_civ) }),200
    else:
        return jsonify({"response":{
         "CIV ": datos_vendedores[0],
         "Vendedores Nombre y Apellido ": datos_vendedores[1] + ' '+ datos_vendedores[2],
         "Fecha de nacimiento ": datos_vendedores [3],
         "Tipo de vendedores ": datos_vendedores[4],
         "Salario ": datos_vendedores[5],
         "Direccion ": datos_vendedores[6],
         "Numero de contacto ": datos_vendedores[7],
         "Porcentaje ": datos_vendedores[8],
         "Monto " : datos_vendedores[9],
         }}),300  


@app.route('/ventas/<int:ventas_cuv>')
def ventas_cuv(ventas_cuv):
    conn = mysql.connect()
    cur = conn.cursor()

    cur.execute('SELECT * FROM ventas WHERE ventas_cuv= %s',(ventas_cuv)) 
    datos_ventas = cur.fetchone()

    if datos_ventas == None:
        return jsonify({"response":"No se encuentran registros con ese ID "+str (ventas_cuv) }),200
    else:
        return jsonify({"response":{
          "CUV": datos_ventas[0],
          "Codigo de Ventas ":datos_ventas [1] ,
          "Numero de contrato ": datos_ventas [2] , 
          "Vendedores ": datos_ventas [3],
          "Clientes ": datos_ventas[4],
          "Monto ": datos_ventas[5],
          "Fecha de venta ": datos_ventas[6],
          "Producto ": datos_ventas[7],
          "Tipo Automovil ": datos_ventas[8] + ", " +  (datos_ventas)[9] + ", " +   (datos_ventas)[10],
         }}),300