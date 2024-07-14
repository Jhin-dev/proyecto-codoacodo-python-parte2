
# Para subir archivo tipo foto al servidor
from werkzeug.utils import secure_filename
import uuid  # Modulo de python para crear un string

from conexion.conexionBD import connectionBD  # Conexión a BD

import datetime
import re
import os

from os import remove  # Modulo  para remover archivo
from os import path  # Modulo para obtener la ruta o directorio

# biblioteca o modulo send_file para forzar la descarga
from flask import send_file


def registro_form_sitio(dataForm, foto_sitio):

    result_foto_sitio = procesar_imagen(foto_sitio)
    try:
        with connectionBD() as conexion_MySQLdb:
            with conexion_MySQLdb.cursor(dictionary=True) as cursor:

                sql = "INSERT INTO tbl_sitios (nombre_sitio, ciudad_sitio, provincia_sitio, descripcion_sitio, foto_sitio) VALUES (%s, %s, %s, %s, %s)"

                # Creando una tupla con los valores del INSERT
                valores = (dataForm['nombre_sitio'], dataForm['ciudad_sitio'], dataForm['provincia_sitio'],
                           dataForm['descripcion_sitio'], result_foto_sitio)
                cursor.execute(sql, valores)

                conexion_MySQLdb.commit()
                resultado_insert = cursor.rowcount
                return resultado_insert

    except Exception as e:
        return f'Se produjo un error en registro_form_sitio: {str(e)}'


def procesar_imagen(foto):
    try:
        # Nombre original del archivo
        filename = secure_filename(foto.filename)
        extension = os.path.splitext(filename)[1]

        # Creando un string de 50 caracteres
        nuevoNameFile = (uuid.uuid4().hex + uuid.uuid4().hex)[:100]
        nombreFile = nuevoNameFile + extension

        # Construir la ruta completa de subida del archivo
        basepath = os.path.abspath(os.path.dirname(__file__))
        upload_dir = os.path.join(basepath, f'../static/fotos_sitios/')

        # Validar si existe la ruta y crearla si no existe
        if not os.path.exists(upload_dir):
            os.makedirs(upload_dir)
            # Dando permiso a la carpeta
            os.chmod(upload_dir, 0o755)

        # Construir la ruta completa de subida del archivo
        upload_path = os.path.join(upload_dir, nombreFile)
        foto.save(upload_path)

        return nombreFile

    except Exception as e:
        print("Error al procesar archivo:", e)
        return []


# Lista de Sitios
def sql_lista_sitiosBD():
    try:
        with connectionBD() as conexion_MySQLdb:
            with conexion_MySQLdb.cursor(dictionary=True) as cursor:
                querySQL = (f"""
                    SELECT 
                        e.id_sitio,
                        e.nombre_sitio, 
                        e.ciudad_sitio,
                        e.provincia_sitio,
                        e.descripcion_sitio,
                        e.foto_sitio
                    FROM tbl_sitios AS e
                    ORDER BY e.id_sitio DESC
                    """)
                cursor.execute(querySQL,)
                sitiosBD = cursor.fetchall()
        return sitiosBD
    except Exception as e:
        print(
            f"Errro en la función sql_lista_sitiosBD: {e}")
        return None


# Detalles de sitio
def sql_detalles_sitiosBD(idSitio):
    try:
        with connectionBD() as conexion_MySQLdb:
            with conexion_MySQLdb.cursor(dictionary=True) as cursor:
                querySQL = ("""
                    SELECT 
                        e.id_sitio,
                        e.nombre_sitio, 
                        e.ciudad_sitio,
                        e.provincia_sitio,
                        e.descripcion_sitio,
                        e.foto_sitio,
                        DATE_FORMAT(e.fecha_registro, '%Y-%m-%d %h:%i %p') AS fecha_registro
                    FROM tbl_sitios AS e
                    WHERE id_sitio =%s
                    ORDER BY e.id_sitio DESC
                    """)
                cursor.execute(querySQL, (idSitio,))
                sitioBD = cursor.fetchone()
        return sitioBD
    except Exception as e:
        print(
            f"Errro en la función sql_detalles_sitiosBD: {e}")
        return None


def buscarSitioBD(search):
    try:
        with connectionBD() as conexion_MySQLdb:
            with conexion_MySQLdb.cursor(dictionary=True) as mycursor:
                querySQL = ("""
                        SELECT 
                            e.id_sitio,
                            e.nombre_sitio, 
                            e.ciudad_sitio,
                            e.provincia_sitio,
                            e.descripcion_sitio,
                            e.foto_sitio
                        FROM tbl_sitios AS e
                        WHERE e.nombre_sitio LIKE %s 
                        ORDER BY e.id_sitio DESC
                    """)
                search_pattern = f"%{search}%"  # Agregar "%" alrededor del término de búsqueda
                mycursor.execute(querySQL, (search_pattern,))
                resultado_busqueda = mycursor.fetchall()
                return resultado_busqueda

    except Exception as e:
        print(f"Ocurrió un error en def buscarSitioBD: {e}")
        return []


def buscarSitioUnico(id):
    try:
        with connectionBD() as conexion_MySQLdb:
            with conexion_MySQLdb.cursor(dictionary=True) as mycursor:
                querySQL = ("""
                        SELECT 
                            e.id_sitio,
                            e.nombre_sitio, 
                            e.ciudad_sitio,
                            e.provincia_sitio,
                            e.descripcion_sitio,
                            e.foto_sitio
                        FROM tbl_sitios AS e
                        WHERE e.id_sitio =%s LIMIT 1
                    """)
                mycursor.execute(querySQL, (id,))
                sitio = mycursor.fetchone()
                return sitio

    except Exception as e:
        print(f"Ocurrió un error en def buscarSitioUnico: {e}")
        return []


def actualizacion_form_sitio(data):
    try:
        with connectionBD() as conexion_MySQLdb:
            with conexion_MySQLdb.cursor(dictionary=True) as cursor:
                nombre_sitio = data.form['nombre_sitio']
                ciudad_sitio = data.form['ciudad_sitio']
                provincia_sitio = data.form['provincia_sitio']
                descripcion_sitio = data.form['descripcion_sitio']
                id_sitio = data.form['id_sitio']

                if data.files['foto_sitio']:
                    file = data.files['foto_sitio']
                    fotoForm = procesar_imagen(file)

                    querySQL = """
                        UPDATE tbl_sitios
                        SET 
                            nombre_sitio = %s,
                            ciudad_sitio = %s,
                            provincia_sitio = %s,
                            descripcion_sitio = %s,
                            foto_sitio = %s
                        WHERE id_sitio = %s
                    """
                    values = (nombre_sitio, ciudad_sitio, provincia_sitio,
                              descripcion_sitio, fotoForm, id_sitio)
                else:
                    querySQL = """
                        UPDATE tbl_sitios
                        SET 
                            nombre_sitio = %s,
                            ciudad_sitio = %s,
                            provincia_sitio = %s,
                            descripcion_sitio = %s
                        WHERE id_sitio = %s
                    """
                    values = (nombre_sitio, ciudad_sitio, provincia_sitio,
                              descripcion_sitio, id_sitio)

                cursor.execute(querySQL, values)
                conexion_MySQLdb.commit()

        return cursor.rowcount or []
    except Exception as e:
        print(f"Ocurrió un error en actualizacion_form_sitio: {e}")
        return None

# Eliminar un sitio
def eliminarSitio(id_sitio, foto_sitio):
    try:
        with connectionBD() as conexion_MySQLdb:
            with conexion_MySQLdb.cursor(dictionary=True) as cursor:
                querySQL = "DELETE FROM tbl_sitios WHERE id_sitio=%s"
                cursor.execute(querySQL, (id_sitio,))
                conexion_MySQLdb.commit()
                resultado_eliminar = cursor.rowcount

                if resultado_eliminar:
                    # Eliminando foto_sitio desde el directorio
                    basepath = path.dirname(__file__)
                    url_File = path.join(
                        basepath, '../static/fotos_sitios', foto_sitio)

                    if path.exists(url_File):
                        remove(url_File)  # Borrar foto desde la carpeta

        return resultado_eliminar
    except Exception as e:
        print(f"Error en eliminarSitio : {e}")
        return []

# Lista de Usuarios creados
def lista_usuariosBD():
    try:
        with connectionBD() as conexion_MySQLdb:
            with conexion_MySQLdb.cursor(dictionary=True) as cursor:
                querySQL = "SELECT id, name_surname, email_user, created_user FROM users"
                cursor.execute(querySQL,)
                usuariosBD = cursor.fetchall()
        return usuariosBD
    except Exception as e:
        print(f"Error en lista_usuariosBD : {e}")
        return []



# Eliminar usuario
def eliminarUsuario(id):
    try:
        with connectionBD() as conexion_MySQLdb:
            with conexion_MySQLdb.cursor(dictionary=True) as cursor:
                querySQL = "DELETE FROM users WHERE id=%s"
                cursor.execute(querySQL, (id,))
                conexion_MySQLdb.commit()
                resultado_eliminar = cursor.rowcount

        return resultado_eliminar
    except Exception as e:
        print(f"Error en eliminarUsuario : {e}")
        return []
