# API de Recetas de Cocina 🍳

## Descripción

Esta API permite gestionar recetas de cocina, ingredientes y categorías. Permite realizar operaciones CRUD para recetas e ingredientes, buscar recetas por ingredientes, y filtrar recetas por tiempo de preparación, dificultad y categoría. Además, los usuarios pueden guardar recetas favoritas.

## Características:
- **Modelos:**

    - Receta: Incluye título, descripción, tiempo de preparación, dificultad, categoría y lista de ingredientes.

    - Ingrediente: Nombre e información adicional sobre los ingredientes.

    - Categoría: Categorías de recetas (e.g. Italiana, Mexicana).

- **Endpoints:**

    - Crear, obtener, actualizar y eliminar recetas.

    - Filtrar recetas por tiempo, dificultad y categoría.

    - Buscar recetas por ingredientes.

    - Guardar recetas favoritas (opcional).

## Requisitos
1. **Python 3.x instalado.**

2. **Django y Django REST Framework.**

3. **django-filter para manejar filtros personalizados.**

## Instalación
1. **Clonar el repositorio**
   Clona este repositorio en tu máquina local:

      ```
      git clone https://github.com/tu_usuario/recetario.git
      cd recetario
      ```
2. **Crear un entorno virtual**
   Si aún no tienes un entorno virtual, crea uno para manejar las dependencias:
      ```
      python -m venv venv
      ```

3. **Activar el entorno virtual**
    En Windows:
    
    ```
    venv\Scripts\activate
    ```


    En Mac/Linux:
    
    ```
    source venv/bin/activate
    ```


4. **Instalar las dependencias**
    Instala las dependencias del proyecto desde requirements.txt:
    
    ```
    pip install -r requirements.txt
    ```


    Si no tienes el archivo requirements.txt, asegúrate de instalar Django y Django REST Framework:
    
    ```
    pip install django djangorestframework django-filter
    ```


5. **Configuración de la base de datos**
   
    Asegúrate de tener la base de datos configurada correctamente en el archivo settings.py de tu proyecto Django.
    
    Realiza las migraciones para crear las tablas necesarias:
    
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```

6. **Ejecutar el servidor de desarrollo**
   
    Para iniciar el servidor de desarrollo, usa el siguiente comando:
    
    ```
    python manage.py runserver
    ```

Esto iniciará la API en http://127.0.0.1:8000/.

## Endpoints
1. **Recetas**
   
    - GET /api/recetas/ - Obtener todas las recetas.
    
    - POST /api/recetas/ - Crear una nueva receta.
    
    - PUT /api/recetas/{id}/ - Actualizar una receta existente.
    
    - DELETE /api/recetas/{id}/ - Eliminar una receta.

2. **Ingredientes**
    - GET /api/ingredientes/ - Obtener todos los ingredientes.
    
    - POST /api/ingredientes/ - Crear un nuevo ingrediente.

3. **Categorías**
   
    - GET /api/categorias/ - Obtener todas las categorías.
    
    - POST /api/categorias/ - Crear una nueva categoría.

## Ejemplo de Solicitudes
**Crear una Receta:**

**Método:** POST

**URL:** http://127.0.0.1:8000/api/recetas/



```
{
  "title": "Spaghetti con Albóndigas",
  "description": "Una receta clásica de pasta con albóndigas de carne.",
  "time_required": 45,
  "difficulty": "Medio",
  "category": 1,  // ID de la categoría
}
```

**Filtrar Recetas:**

**Método:** GET
**URL:**
```
http://127.0.0.1:8000/api/recetas/
```



## Contribuciones
Si deseas contribuir al proyecto, por favor abre un pull request con una descripción detallada de los cambios que propones.

## Licencia
Este proyecto está bajo la Licencia MIT.
