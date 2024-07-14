from app import app
from flask import render_template, request, flash, redirect, url_for, session,  jsonify
from mysql.connector.errors import Error


# Importando cenexión a BD
from controllers.funciones_home import *

PATH_URL = "public/sitios"


@app.route('/registrar-sitio', methods=['GET'])
def viewFormSitio():
    if 'conectado' in session:
        return render_template(f'{PATH_URL}/form_sitio.html')
    else:
        flash('primero debes iniciar sesión.', 'error')
        return redirect(url_for('inicio'))


@app.route('/form-registrar-sitio', methods=['POST'])
def formSitio():
    if 'conectado' in session:
        if 'foto_sitio' in request.files:
            foto_sitio = request.files['foto_sitio']
            resultado = registro_form_sitio(request.form, foto_sitio)
            if resultado:
                return redirect(url_for('lista_sitios'))
            else:
                flash('El sitio NO fue creado.', 'error')
                return render_template(f'{PATH_URL}/form_sitio.html')
    else:
        flash('primero debes iniciar sesión.', 'error')
        return redirect(url_for('inicio'))


@app.route('/lista-de-sitios', methods=['GET'])
def lista_sitios():
    if 'conectado' in session:
        return render_template(f'{PATH_URL}/lista_sitios.html', sitios=sql_lista_sitiosBD())
    else:
        flash('primero debes iniciar sesión.', 'error')
        return redirect(url_for('inicio'))


@app.route("/detalles-sitio/", methods=['GET'])
@app.route("/detalles-sitio/<int:idSitio>", methods=['GET'])
def detalleSitio(idSitio=None):
    if 'conectado' in session:
        # Verificamos si el parámetro idSitio es None o no está presente en la URL
        if idSitio is None:
            return redirect(url_for('inicio'))
        else:
            detalle_sitio = sql_detalles_sitiosBD(idSitio) or []
            return render_template(f'{PATH_URL}/detalles_sitio.html', detalle_sitio=detalle_sitio)
    else:
        flash('Primero debes iniciar sesión.', 'error')
        return redirect(url_for('inicio'))


# Buscadon de sitios
@app.route("/buscando-sitio", methods=['POST'])
def viewBuscarSitioBD():
    resultadoBusqueda = buscarSitioBD(request.json['busqueda'])
    if resultadoBusqueda:
        return render_template(f'{PATH_URL}/resultado_busqueda_sitio.html', dataBusqueda=resultadoBusqueda)
    else:
        return jsonify({'fin': 0})


@app.route("/editar-sitio/<int:id>", methods=['GET'])
def viewEditarSitio(id):
    if 'conectado' in session:
        respuestaSitio = buscarSitioUnico(id)
        if respuestaSitio:
            return render_template(f'{PATH_URL}/form_sitio_update.html', respuestaSitio=respuestaSitio)
        else:
            flash('El sitio no existe.', 'error')
            return redirect(url_for('inicio'))
    else:
        flash('Primero debes iniciar sesión.', 'error')
        return redirect(url_for('inicio'))


# Recibir formulario para actulizar informacion de sitio
@app.route('/actualizar-sitio', methods=['POST'])
def actualizarSitio():
    resultData = actualizacion_form_sitio(request)
    if resultData:
        return redirect(url_for('lista_sitios'))


@app.route("/lista-de-usuarios", methods=['GET'])
def usuarios():
    if 'conectado' in session:
        resp_usuariosBD = lista_usuariosBD()
        return render_template('public/usuarios/lista_usuarios.html', resp_usuariosBD=resp_usuariosBD)
    else:
        return redirect(url_for('inicioCpanel'))


@app.route('/borrar-usuario/<string:id>', methods=['GET'])
def borrarUsuario(id):
    resp = eliminarUsuario(id)
    if resp:
        flash('El Usuario fue eliminado correctamente', 'success')
        return redirect(url_for('usuarios'))


@app.route('/borrar-sitio/<string:id_sitio>/<string:foto_sitio>', methods=['GET'])
def borrarSitio(id_sitio, foto_sitio):
    resp = eliminarSitio(id_sitio, foto_sitio)
    if resp:
        flash('El Sitio fue eliminado correctamente', 'success')
        return redirect(url_for('lista_sitios'))
