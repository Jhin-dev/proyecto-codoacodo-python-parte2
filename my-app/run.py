# Declarando nombre de la aplicación e inicializando, crear la aplicación Flask
from decouple import config

# Importando todos mis Routers (Rutas)
from routers.router_login import *
from routers.router_home import *
from routers.router_page_not_found import *

def create_app():
    init = app
    return init

# Ejecutando el objeto Flask
if __name__ == '__main__':
    init = create_app()
    init.run(debug=True, port=config('PORT'))
