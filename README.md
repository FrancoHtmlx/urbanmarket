# 🛍️ UrbanMarket - E-commerce Platform

Una plataforma de comercio electrónico moderna y completa desarrollada con Django, que ofrece una experiencia de compra intuitiva y un diseño responsive.

![UrbanMarket](https://img.shields.io/badge/Django-4.2+-green.svg)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-blue.svg)
![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)

## 🚀 Características Principales

- **🛒 Carrito de Compras**: Sistema completo de carrito con gestión de cantidades
- **👤 Autenticación de Usuarios**: Registro, login y gestión de perfiles
- **📱 Diseño Responsive**: Optimizado para dispositivos móviles y desktop
- **🏷️ Gestión de Productos**: Catálogo organizado por categorías
- **💳 Sistema de Checkout**: Proceso de compra simplificado
- **🎨 UI/UX Moderna**: Interfaz atractiva con Bootstrap 5 y Font Awesome
- **🔍 Búsqueda y Filtros**: Navegación intuitiva por productos
- **📊 Panel de Administración**: Gestión completa desde Django Admin

## 🛠️ Tecnologías Utilizadas

### Backend
- **Django 4.2+** - Framework web de Python
- **SQLite** - Base de datos (configurable para PostgreSQL/MySQL)
- **Python 3.8+** - Lenguaje de programación

### Frontend
- **HTML5 & CSS3** - Estructura y estilos
- **Bootstrap 5.3** - Framework CSS responsive
- **JavaScript** - Interactividad del lado del cliente
- **Font Awesome** - Iconografía

### Herramientas
- **Django Admin** - Panel de administración
- **Django Forms** - Manejo de formularios
- **Django Authentication** - Sistema de usuarios

## 📦 Instalación y Configuración

### Prerrequisitos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/tu-usuario/urbanmarket.git
   cd urbanmarket
   ```

2. **Crear entorno virtual**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar la base de datos**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Crear superusuario (opcional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Ejecutar el servidor de desarrollo**
   ```bash
   python manage.py runserver
   ```

7. **Acceder a la aplicación**
   - Aplicación: http://127.0.0.1:8000/
   - Admin: http://127.0.0.1:8000/admin/

## 📱 Screenshots

### Página Principal
![Home Page](screenshots/home.png)

### Catálogo de Productos
![Products](screenshots/products.png)

### Carrito de Compras
![Cart](screenshots/cart.png)

### Detalle del Producto
![Product Detail](screenshots/product-detail.png)

## 🏗️ Estructura del Proyecto

```
UrbanMarket/
├── Aplicaciones/
│   └── Tienda/
│       ├── models.py          # Modelos de datos
│       ├── views.py           # Lógica de vistas
│       ├── urls.py            # URLs de la aplicación
│       ├── forms.py           # Formularios
│       ├── admin.py           # Configuración del admin
│       └── templates/         # Plantillas HTML
├── Proyecto2/
│   ├── settings.py            # Configuración de Django
│   ├── urls.py                # URLs principales
│   └── wsgi.py                # Configuración WSGI
├── media/                     # Archivos multimedia
├── static/                    # Archivos estáticos
├── manage.py                  # Script de gestión de Django
└── requirements.txt           # Dependencias del proyecto
```

## 🎯 Funcionalidades Detalladas

### Para Usuarios
- ✅ Registro y autenticación de usuarios
- ✅ Navegación por categorías de productos
- ✅ Búsqueda de productos
- ✅ Visualización detallada de productos
- ✅ Agregar productos al carrito
- ✅ Gestión del carrito de compras
- ✅ Proceso de checkout
- ✅ Historial de pedidos
- ✅ Gestión de perfil de usuario

### Para Administradores
- ✅ Panel de administración completo
- ✅ Gestión de productos y categorías
- ✅ Gestión de usuarios y pedidos
- ✅ Subida de imágenes de productos
- ✅ Estadísticas básicas

## 🚀 Próximas Mejoras

- [ ] Sistema de reseñas y calificaciones
- [ ] Integración con pasarelas de pago
- [ ] Sistema de cupones y descuentos
- [ ] Notificaciones por email
- [ ] API REST para aplicaciones móviles
- [ ] Sistema de wishlist
- [ ] Chat de soporte en vivo

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Para contribuir:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 👨‍💻 Autor

**Francisco** - [Tu LinkedIn](https://linkedin.com/in/tu-perfil) - [Tu Email](mailto:tu-email@ejemplo.com)

## 🙏 Agradecimientos

- Django Community por el excelente framework
- Bootstrap Team por el framework CSS
- Font Awesome por los iconos
- Todos los contribuidores de código abierto

---

⭐ **¡Si te gusta este proyecto, dale una estrella en GitHub!** ⭐