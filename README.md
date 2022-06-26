# Proyecto "pagina tipo blog": "MyCoderSpace" para trabajo final de CoderHouse por Alejandro Barrios y Alvaro Marcano

Entrega final para curso de python de CoderHouse con temática de "pagina tipo blog". 

Dedicimos llamarlo MyCoderSpace en alusión a MySpace en la cual el propósito es ofrecer un blog/red social en el cual pueden reunirse los programadores y 
compartir experiencias cotidianas o discutir sus proyectos

## Se conforma por:

* ### Pagina principal ("/")

#### Barra de navegación

Observamos la barra de navegación con el nombre de la página, logo, botón de agregar nuevo blog y botones de navegación que cambian dependiendo si el usuario está o no
loggeado

#### Blogs

En el centro visualizamos la lista de entradas de blog compuestas por el modelo BlogModel el cual consiste en entradas de blog que contienen: Título, 
Subtítulo, Cuerpo, Autor, Fecha de publicación e Imagen .

Veremos el cuerpo incompleto y finalizado con puntos suspensivos (...) que podremos ver en detalle al hacer click en Título. Y veremos en la parte superior derecha
de cada entrada un botón de editar blog (icono de lapiz) y un botón de borrar blog (icono de "x")

* ### Perfil de usuario ("profile/")

Se observa modelo **Blogger** y **Avatar** el cual nos muestra el avatar del usuario y su información personal: Nombre, Apellido, Correo electrónico

* ### Crear Blog ("create/")

Nos muestra el formulario de creación de blogs donde introducimos nuestros datos y la URL de la imagen que queremos adjuntar. La fecha de creación y el nombre de
usuario son creados automáticamente por el sistema

* ### Crear Usuario y Login ("signup/" - "signin/")

Se accede por la barra de navegación y solo son visibles cuando el usuario no está loggeado

## Distribución de Tareas

* ### Alejandro Barrios 
1. Creacion de CRUD de Blogs en views
2. Creacion de Modelo de Blog
3. Creacion de plantilla de About Us
4. Creado UserMixing de blogs

* ### Alvaro Marcano
1. Creado sistema de Login, Logout, SignUp
2. Creadas plantillas de blog y de perfiles incluyendo HTML/CSS
3. Agregado Modelo y Sistema de Avatares
4. Creados casos de prueba
5. Creacion de README
