# Challenge BackEnd - Agencia EGO

## Se debe construir:

1. Modelos e interfaces de administración
necesarias para agregar, modificar y eliminar
los datos mostrados en el ejemplo
2. Endpoints de API necesarios para consumir
los datos
3. Entregable en repositorio GIT, basado en el siguiente mock-up:
    https://www.figma.com/file/GXTK5WFOuIYtRqRFpIaepH/Test_Dev?node-id=0%3A1

## Instalación:
1. Asegúrese de tener creado y activado un entorno virtual con [Virtualenv](https://virtualenv.pypa.io/en/latest/) o [VirtualenvWrapper](https://virtualenvwrapper.readthedocs.io/en/latest/). Versión requerida Python3.8+
2. Clone el proyecto desde el repositorio:
```sh
git clone https://github.com/cristianjs19/Toyota-API-Challenge.git
```
3. Diríjase a la carperta donde se encuentra el archivo requirements.txt e instale las dependencias:
```sh
pip install -r requirements.txt
```
4. El repositorio cuenta con una base de datos de prueba con algunos datos cargados, por lo que puede dirigirse a la carpeta raiz del proyecto e iniciar el servidor con el comando `python manage.py runserver`. Esta base de datos cuenta con un usuario:  
username: cristian  
password: eerr  
Con el que podrá comenzar a utilizar el proyecto.
5. Si desea iniciar una base de datos propia, puede eliminar la base de datos existente y correr el comando `python manage.py migrate`. Luego se recomienda también crear un superusuario `python manage.py createsuperuser` con el cual podrá acceder al panel de administración localizado en la dirección `http://127.0.0.1:8000/admin`.

## Extras:
##### Documentación de API: `http://127.0.0.1:8000/swagger/`
Nota: La documentación ofrece la posibilidad de interactuar con cada endpoint desde el botón "try it out".
##### Ejecución de tests: `python manage.py test`

