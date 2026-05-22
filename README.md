# Aplicación de E-commerce Mundo Deporte

Este repositorio contiene una aplicación de e-commerce full-stack llamada "Mundo Deporte", desarrollada como un proyecto para Programación 3 - 2025. La aplicación cuenta con un catálogo de productos, autenticación de usuarios, un carrito de compras y una simulación de pago con gestión de stock.

## Tabla de Contenidos

- [Requisitos Previos](#requisitos-previos)
- [Características](#características)
- [Tecnologías Utilizadas](#tecnologías-utilizadas)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Configuración e Instalación](#configuración-e-instalación)
  - [Configuración del Backend](#configuración-del-backend)
  - [Configuración del Frontend](#configuración-del-frontend)
- [Ejecutando la Aplicación](#ejecutando-la-aplicación)
- [Ejecución con Docker (Recomendado)](#ejecución-con-docker-recomendado)
- [Endpoints de la API](#endpoints-de-la-api)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)

## Requisitos Previos

Antes de instalar y ejecutar este proyecto, asegúrate de tener instalado lo siguiente:

### Para el Backend
- **Python:** Versión 3.13.5
  - Verifica tu versión: `python3 --version`
- **pip:** Gestor de paquetes de Python (generalmente viene con Python): version: pip 25.1.1
  - Verifica tu versión: `pip --version`

### Para el Frontend
- **Node.js:** Versión 20.19.2
  - Verifica tu versión: `node --version`
- **npm:** Versión 9.2.0
  - Verifica tu versión: `npm --version`

### Herramientas Adicionales (Opcional pero Recomendado)
- **Git:** Para clonar y gestionar el repositorio
  - [Descargar Git](https://git-scm.com/)
- **VS Code:** Editor de código recomendado
  - [Descargar VS Code](https://code.visualstudio.com/)
  - Extensión recomendada: **REST Client** (para probar los endpoints)

## Características

- **Autenticación de Usuarios:** Funcionalidad de registro, inicio y cierre de sesión.
- **Catálogo de Productos:** Navegar y ver detalles de varios productos.
- **Carrito de Compras:** Añadir, eliminar y actualizar cantidades de productos en el carrito.
- **Gestión de Stock:** Las cantidades de los productos se actualizan después de una compra exitosa.
- **Simulación de Pago:** Un paso de confirmación antes de finalizar una compra.
- **Usuarios:** Cada usuario puede vender productos y además ver compras pasadas

## Tecnologías Utilizadas

### Frontend
- **React:** Una biblioteca de JavaScript para construir interfaces de usuario.
- **Vite:** Una herramienta de construcción rápida para proyectos web modernos.
- **React Router DOM:** Para enrutamiento declarativo en aplicaciones React.
- **Axios:** Para realizar peticiones HTTP.
- **CSS:** Para estilizar la aplicación.

### Backend
- **FastAPI:** Un framework web moderno y rápido (de alto rendimiento) para construir APIs con Python 3.7+ basado en las anotaciones de tipo estándar de Python.
- **SQLAlchemy:** Un kit de herramientas SQL y Mapeador Objeto-Relacional (ORM) que brinda a los desarrolladores de aplicaciones todo el poder y la flexibilidad de SQL.
- **PostgreSQL:** Un sistema de gestión de bases de datos relacionales de objetos de código abierto potente y profesional (utilizado en el entorno Docker).
- **SQLite:** Utilizado para desarrollo local rápido fuera de Docker.
- **Uvicorn:** Un servidor ASGI para Python.
- **Alembic:** Una herramienta de migración de bases de datos para SQLAlchemy.
- **PyJWT:** Para la implementación de JSON Web Token (JWT) para autenticación.
- **Passlib:** Para el hashing de contraseñas.

## Estructura del Proyecto

El proyecto se divide en dos partes principales: `backend` y `frontend`.

```
.
├── backend/
│   ├── alembic/                  # Migraciones de la base de datos
│   ├── app/                      # Aplicación FastAPI
│   │   ├── database/             # Conexión y modelos de la base de datos
│   │   ├── models/               # Modelos ORM de SQLAlchemy
│   │   ├── routes/               # Endpoints de la API
│   │   └── schemas/              # Esquemas Pydantic para validación de datos
│   ├── auth.py                   # Lógica de autenticación
│   ├── requirements.txt          # Dependencias de Python del backend
│   └── README.md                 # Documentación específica del backend
├── frontend/
│   ├── public/                   # Archivos estáticos
│   ├── src/                      # Código fuente de la aplicación React
│   │   ├── assets/               # Imágenes y otros recursos
│   │   ├── components/           # Componentes de React reutilizables
│   │   ├── context/              # Context de React para gestión de estado
│   │   ├── App.css               # Estilos globales
│   │   ├── App.jsx               # Componente principal de la aplicación
│   │   ├── index.css             # CSS base
│   │   └── main.jsx              # Punto de entrada de la aplicación React
│   ├── package.json              # Dependencias de Node.js del frontend
│   └── README.md                 # Documentación específica del frontend
└── README.md                     # README principal del proyecto
```

## Configuración e Instalación

Sigue estos pasos para tener el proyecto funcionando en tu máquina local.

### Configuración del Entorno

Antes de ejecutar la aplicación, necesitas configurar las variables de entorno tanto para el backend como para el frontend.

**Para el backend:**
Asegurate de estar en la **carpeta raíz del proyecto**, es decir, la carpeta donde se encuentra el directorio `backend y frontend`.
1.  Navega al directorio `backend`:
    ```bash
    cd backend
    ```
2.  Crea un nuevo archivo llamado `.env`:
    ```bash
    touch .env
    ```
3.  Abre el archivo `.env` y actualiza las variables según sea necesario. El contenido debería ser similar a esto:
    ```
    # Configuración del Backend
    DATABASE_URL="sqlite:///./app/database/mundodeporte.db"
    SECRET_KEY="tu_clave_super_secreta_aqui"
    ```
    -   `DATABASE_URL`: La cadena de conexión para tu base de datos. El valor por defecto está configurado para SQLite.
    -   `SECRET_KEY`: Una clave secreta para la generación de tokens JWT. Se recomienda usar una cadena larga y aleatoria.

**Para el frontend:**
Asegurate de estar en la **carpeta raíz del proyecto**, es decir, la carpeta donde se encuentra el directorio `frontend y backend`.

1.  Navega al directorio `frontend`:
    ```bash
    cd frontend
    ```
2.  Crea un nuevo archivo llamado `.env`:
    ```bash
    touch .env
    ```
3.  El archivo `.env` debe contener la URL de tu API de backend:
    ```
    # Configuración del Frontend
    VITE_API_URL=http://localhost:8000
    ```
    -   `VITE_API_URL`: La URL de la API del backend. El valor por defecto es `http://localhost:8000`.

### Configuración del Backend
Abre una terminal en la **carpeta raíz del proyecto**, es decir, la carpeta donde se encuentra el directorio `backend y frontend`.

1.  **Navega al directorio del backend:**
    ```bash
    cd backend
    ```

2.  **Crea un entorno virtual (recomendado):**
    ```bash
    python3 -m venv venv
    ```

3.  **Activa el entorno virtual:**
    ```bash
    source venv/bin/activate
    ```

4.  **Instala las dependencias del backend:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Inicia el servidor del backend:**
    ```bash
    uvicorn app.main:app --reload --port 8000
    ```
    La API del backend estará disponible en `http://localhost:8000`.

### Configuración del Frontend
Abre otra terminal en la **carpeta raíz del proyecto**, es decir, la carpeta donde se encuentra el directorio `frontend y backend`.

1.  **Navega al directorio del frontend:**
    ```bash
    cd frontend
    ```

2.  **Instala las dependencias del frontend:**
    ```bash
    npm install
    ```

3.  **Inicia el servidor de desarrollo del frontend:**
    ```bash
    npm run dev
    ```
    La aplicación del frontend estará disponible en `http://localhost:5173` (u otro puerto si el 5173 está en uso).

## Ejecución con Docker (Recomendado)

Esta es la forma más rápida y robusta de poner en marcha todo el proyecto. Se utiliza un entorno orquestado con **Docker Compose** que incluye el frontend (Nginx), el backend (FastAPI) y la base de datos (PostgreSQL).

### Pasos rápidos:

1.  Asegúrate de estar en la raíz del proyecto.
2.  Ejecuta el siguiente comando para construir y levantar los contenedores:
    ```bash
    docker compose up --build
    ```
    *Nota: Si recibes un error de `permission denied` al conectar al socket de Docker, intenta usar `sudo docker compose up --build` o [agrega tu usuario al grupo docker](https://docs.docker.com/engine/install/linux-postinstall/).*

3.  ¡Listo! Ya puedes acceder a la aplicación:
    -   **Frontend:** [http://localhost](http://localhost) (Puerto 80)
    -   **Backend (Docs):** [http://localhost/api/docs](http://localhost/api/docs)
    -   **API Base:** [http://localhost/api/](http://localhost/api/)

### Detalles de la arquitectura Docker:
-   **Frontend:** Se compila la aplicación Vite y se sirve mediante **Nginx**. Este contenedor también actúa como **Proxy Inverso**, redirigiendo las peticiones de `/api/*` al contenedor del backend.
-   **Backend:** Ejecuta FastAPI de forma aislada, comunicándose con la base de datos por la red interna de Docker.
-   **Base de datos:** Utiliza **PostgreSQL 15**. Los datos persisten en un volumen de Docker llamado `db_data`.
-   **Puerto único:** Todo el sistema se expone únicamente a través del **puerto 80**.

## Ejecutando la Aplicación

1.  Asegúrate de que tanto el servidor del backend como el del frontend estén funcionando en instancias de terminal separadas.
2.  Abre tu navegador web y navega a la URL del frontend (ej., `http://localhost:5173`).

## Endpoints de la API

El backend proporciona los siguientes endpoints de la API REST:

### Autenticación
- **POST** `/auth/register` - Registrar un nuevo usuario
- **POST** `/auth/login` - Autenticar un usuario y obtener un token JWT
- **GET** `/auth/protected` - Acceder a una ruta protegida (requiere autenticación)
- **GET** `/auth/me` - Obtener información del usuario actual (requiere autenticación)

### Productos (Lectura)
- **GET** `/products/` - Obtener todos los productos (soporta filtrado por `min_price` y `max_price`)
- **GET** `/products/{id}` - Obtener un producto específico por ID

### Productos (Escritura - Requiere Autenticación)
- **POST** `/products/` - Crear un nuevo producto
- **PUT** `/products/{id}` - Actualizar un producto existente
- **DELETE** `/products/{id}` - Eliminar un producto

### Gestión de Stock
- **PUT** `/products/{id}/stock` - Actualizar el stock de un producto

### Compras
- **POST** `/purchases/` - Crear una nueva compra (requiere autenticación)
- **GET** `/purchases/me` - Obtener todas las compras del usuario actual (requiere autenticación)

### Información General
- **GET** `/` - Obtener información de bienvenida de la API

> 💡 **Nota:** Para probar todos los endpoints de forma interactiva, consulta el archivo `backend/tests/requests.http` que es compatible con la extensión REST Client de VS Code.