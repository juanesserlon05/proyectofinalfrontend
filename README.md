# ToDoList - Proyecto Django

Este es un proyecto simple de lista de tareas (todolist) desarrollado con Django, HTML, CSS y JavaScript.

## Configuración del Entorno Virtual (venv)

Para evitar conflictos de dependencias, es recomendable utilizar un entorno virtual. A continuación se describen los pasos para configurar el entorno virtual y instalar Django:

1. Abre una terminal en la carpeta raíz del proyecto.

2. Ejecuta el siguiente comando para crear un entorno virtual:

   python -m venv venv
Activa el entorno virtual:

En Windows:

.\venv\Scripts\activate

En Linux/Mac:

source venv/bin/activate

Una vez activado el entorno virtual, instala las dependencias utilizando el siguiente comando:

pip install -r requirements.txt
Instalación de Django
Después de configurar el entorno virtual, instala Django con el siguiente comando:

pip install 

Ejecutar el Proyecto
Asegúrate de haber activado el entorno virtual.

Aplica las migraciones de la base de datos:

python manage.py migrate
Crea un superusuario (admin) para acceder al panel de administración (opcional):

python manage.py createsuperuser

Inicia el servidor de desarrollo:

python manage.py runserver
Abre tu navegador y visita http://localhost:8000/ para ver la aplicación.

Tecnologías Utilizadas
Django
HTML
CSS
JavaScript
Contribuciones
¡Contribuciones son bienvenidas! Si encuentras algún problema o tienes sugerencias, por favor, crea un "issue" en el repositorio.
