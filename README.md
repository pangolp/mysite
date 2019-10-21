# MySite

Tutorial de Django, basado un poco en la documentación oficial.

# Instalación

```sh
$ git clone https://github.com/pangolp/mysite.git 
```
### Dependencias

Recuerde que todas las dependencias se encuentran en el fichero llamado requirements.txt y que la mejor forma de correr el proyecto es través de un entorno virtual.

```
$ python -m venv entorno
$ entorno\Scripts\activate
$ pip install -r requirements.txt
```

### Documentación

* [Django 2.2](https://docs.djangoproject.com/en/2.2/)
* [Bootstrap](https://getbootstrap.com/)
* [Pillow](https://pillow.readthedocs.io/en/stable/installation.html)
* [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)

### Recuerden aplicar migraciones.

```sh
$ python manage.py migrate
```

### Servidor de desarrollo, a través del comando:

```sh
$ python manage.py runserver
```
### Borrar las carpetas __pycache__ del proyecto
```sh
$ find . -type d -name __pycache__ -exec rm -r {} \+
```
