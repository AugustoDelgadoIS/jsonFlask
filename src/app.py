from flask import Flask, jsonify, request
from config import config
from flask_mysqldb import MySQL
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'MIIRfONIC'

login_manager =LoginManager (app)

conexion = MySQL(app)


@app.route('/cursos', methods=['GET'])
def listar_cursos():
    try:
        cursor = conexion.connection.cursor()
        sql = "select * from cursos"
        cursor.execute(sql)
        datos = cursor.fetchall()
        cursos = []
        for fila in datos:
            curso = {'codigo': fila[0], 'nombre': fila[1], 'creditos': fila[2]}
            cursos.append(curso)
        return jsonify({'cursos': cursos, 'mensaje': "Cursos listados."})

    except Exception as ex:
        return jsonify({'mensaje': "Error"})


@app.route('/cursos/<codigo>', methods=['GET'])
def leer_curso(codigo):
    try:
        cursor = conexion.connection.cursor()
        sql = "select * from cursos where codigo = '{0}'".format(codigo)
        cursor.execute(sql)
        datos = cursor.fetchone()
        if datos != None:
            curso = {'codigo': datos[0],
                     'nombre': datos[1], 'creditos': datos[2]}
            return jsonify({'cursos': curso, 'mensaje': "Cursos Encontrado."})
        else:
            return jsonify({'mensaje': "Curso no Encontrado"})
    except Exception as ex:
        return jsonify({'mensaje': "Error"})


@app.route('/cursos', methods=['POST'])
def registrar_curso():
    # print(request.json)
    try:
        cursor = conexion.connection.cursor()
        sql = """insert into  cursos (codigo, nombre, creditos) 
        values ('{0}','{1}',{2})""".format(request.json['codigo'], request.json['nombre'], request.json['creditos'])

        cursor.execute(sql)
        conexion.connection.commit()  # copnfirma la accion de insercion.

        return jsonify({'mensaje': "Curso Registrado"})
    except Exception as ex:
        return jsonify({'mensaje': "Error"})


@app.route('/cursos/<codigo>', methods=['PUT'])
def actualizar_curso(codigo):
    try:
        cursor = conexion.connection.cursor()
        sql = """UPDATE cursos SET nombre = '{0}', creditos = '{1}' WHERE codigo = '{2}' """.format(request.json['nombre'], request.json['creditos'],codigo)
        cursor.execute(sql)
        conexion.connection.commit()  # copnfirma la accion de insercion.
        return jsonify({'mensaje': "Curso Actualizado."})
    except Exception as ex:
        return jsonify({'mensaje': "HORROR"})


@app.route('/cursos/<codigo>', methods=['DELETE'])
def eliminar_curso(codigo):
    try:
        cursor = conexion.connection.cursor()
        sql = "DELETE FROM cursos where codigo = '{0}'".format(codigo)
        cursor.execute(sql)
        conexion.connection.commit()  # copnfirma la accion de insercion.

        return jsonify({'mensaje': "Curso Eliminado"})
    except Exception as ex:
        return jsonify({'mensaje': "Error"})


def pagina_no_encontrada(error):
    return "<h1> la pagina que intentas buscar no existe... </h1>", 404


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, pagina_no_encontrada)
    app.run (host='0.0.0.0', port=5000)
