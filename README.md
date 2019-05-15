# MySite

Tutorial de Django, basado un poco en la documentación oficial.

# Instalación

```sh
$ git clone https://github.com/pangolp/mysite.git 
```
### Dependencias

Recuerde que todas las dependencias se encuentran en el fichero llamado requirements.txt y que la mejor forma de correr el proyecto es través de un entorno virtual.

```
$ python -m venv **entorno** # el nombre que ustedes deseen del entorno virtual
$ # Deben de activar el entorno virtual
$ entorno\Scripts\activate
# # Ingresan a donde se encuentra el fichero requirements.txt
$ pip install -r requirements.txt
```

### Documentación

* [Django 2.2](https://docs.djangoproject.com/en/2.2/)
* [Bootstrap](https://getbootstrap.com/)
* [Pillow](https://pillow.readthedocs.io/en/stable/installation.html)

Recuerden aplicar migraciones.

```sh
$ python manage.py migrate
```

Servidor de desarrollo, a través del comando:

```sh
$ python manage.py runserver
```
