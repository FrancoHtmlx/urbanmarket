from django.urls import path
from . import views

urlpatterns = [
    # Página principal
    path('', views.home, name='home'),
    
    # Categorías
    path('categorias/', views.categorias, name='categorias'),
    path('categoria/<int:categoria_id>/', views.categoria_productos, name='categoria_productos'),

    # Productos
    path('productos/', views.productos, name='productos'),
    path('producto/<int:producto_id>/', views.producto_detalle, name='producto_detalle'),

    # Clientes
    path('clientes/', views.clientes, name='clientes'),
    path('cliente/<int:cliente_id>/', views.cliente_detalle, name='cliente_detalle'),

    # Pedidos
    path('pedidos/', views.pedidos, name='pedidos'),
    path('pedido/<int:pedido_id>/', views.pedido_detalle, name='pedido_detalle'),

    # Detalle del Pedido
    path('detalle_pedido/<int:pedido_id>/', views.detalle_pedido, name='detalle_pedido'),
    
    # Detalle del Producto
    path('producto/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),
    
    # Carrito de compras
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('carrito/agregar/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/actualizar/<int:producto_id>/', views.actualizar_carrito, name='actualizar_carrito'),
    path('carrito/eliminar/<int:producto_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
    path('carrito/vaciar/', views.vaciar_carrito, name='vaciar_carrito'),
    
    # Checkout
    path('checkout/', views.checkout, name='checkout'),
    
    # Autenticación
    path('registro/', views.registro_usuario, name='registro_usuario'),
    path('login/', views.login_usuario, name='login_usuario'),
    path('logout/', views.logout_usuario, name='logout_usuario'),
    path('perfil/', views.perfil_usuario, name='perfil_usuario'),
    ]
