from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.core.paginator import Paginator
from django.utils import timezone
from .models import Categoria, Producto, Cliente, Pedido, DetallePedido, OrdenCompra, DetalleOrden
from .forms import RegistroForm, LoginForm

# Vista de inicio
def home(request):
    productos_destacados = Producto.objects.filter(destacado=True)[:6]  # Solo los destacados
    return render(request, 'home.html', {'productos_destacados': productos_destacados})


# Categorías
def categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'categorias.html', {'categorias': categorias})

# Productos de una categoría específica
def categoria_productos(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    productos = categoria.productos.all()

    # Búsqueda
    query = request.GET.get('q')
    if query:
        productos = productos.filter(nombre__icontains=query)

    # Filtro por precio
    min_precio = request.GET.get('min_precio')
    max_precio = request.GET.get('max_precio')
    if min_precio:
        productos = productos.filter(precio__gte=min_precio)
    if max_precio:
        productos = productos.filter(precio__lte=max_precio)

    # Filtro por stock disponible
    stock = request.GET.get('stock')
    if stock == 'disponible':
        productos = productos.filter(stock__gt=0)

    # Ordenamiento
    orden = request.GET.get('orden')
    if orden == 'precio_asc':
        productos = productos.order_by('precio')
    elif orden == 'precio_desc':
        productos = productos.order_by('-precio')

    # Paginación: 6 productos por página
    paginator = Paginator(productos, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'categoria_productos.html', {
        'categoria': categoria,
        'productos': page_obj,
        'min_precio': min_precio or '',
        'max_precio': max_precio or '',
        'stock': stock or '',
        'query': query or '',
        'orden': orden or ''
    })


# Listado de productos
def productos(request):
    productos = Producto.objects.all()

    # Búsqueda
    query = request.GET.get('q')
    if query:
        productos = productos.filter(nombre__icontains=query)

    # Filtro por precio
    min_precio = request.GET.get('min_precio')
    max_precio = request.GET.get('max_precio')
    if min_precio:
        productos = productos.filter(precio__gte=min_precio)
    if max_precio:
        productos = productos.filter(precio__lte=max_precio)

    # Filtro por stock disponible
    stock = request.GET.get('stock')
    if stock == 'disponible':
        productos = productos.filter(stock__gt=0)

    # Ordenamiento
    orden = request.GET.get('orden')
    if orden == 'precio_asc':
        productos = productos.order_by('precio')
    elif orden == 'precio_desc':
        productos = productos.order_by('-precio')

    # Paginación: 6 productos por página
    paginator = Paginator(productos, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'productos.html', {
        'productos': page_obj,
        'query': query or '',
        'min_precio': min_precio or '',
        'max_precio': max_precio or '',
        'stock': stock or '',
        'orden': orden or ''
    })




# Detalle de producto
def producto_detalle(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return render(request, 'producto_detalle.html', {'producto': producto})

# Listado de clientes
def clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes.html', {'clientes': clientes})

# Detalle de cliente
def cliente_detalle(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    return render(request, 'cliente_detalle.html', {'cliente': cliente})

# Listado de pedidos
def pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'pedidos.html', {'pedidos': pedidos})

# Detalle de pedido
def pedido_detalle(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    return render(request, 'pedido_detalle.html', {'pedido': pedido})

# Detalle de pedido específico
def detalle_pedido(request, pedido_id):
    detalle = DetallePedido.objects.filter(pedido_id=pedido_id)
    return render(request, 'detalle_pedido.html', {'detalle': detalle})

# ------------------------------
# Vistas de checkout
# ------------------------------
def checkout(request):
    carrito = request.session.get('carrito', {})

    productos_carrito = []
    total = 0
    for producto_id, cantidad in carrito.items():
        producto = get_object_or_404(Producto, id=producto_id)
        subtotal = producto.precio * cantidad
        total += subtotal
        productos_carrito.append({
            'producto': producto,
            'cantidad': cantidad,
            'subtotal': subtotal
        })

    if request.method == 'POST':
        direccion = request.POST.get('direccion')
        
        # Si el usuario está autenticado, usar sus datos
        if request.user.is_authenticated:
            usuario = request.user
            nombre_cliente = f"{usuario.first_name} {usuario.last_name}".strip() or usuario.username
            email_cliente = usuario.email
        else:
            # Si no está autenticado, usar datos del formulario
            usuario = None
            nombre_cliente = request.POST.get('nombre_cliente', 'Cliente Anónimo')
            email_cliente = request.POST.get('email_cliente', '')

        # Crear orden
        orden = OrdenCompra.objects.create(
            usuario=usuario,
            total=total,
            direccion_envio=direccion,
            estado="Pendiente"
        )

        # Guardar detalle de cada producto en la orden
        for item in productos_carrito:
            DetalleOrden.objects.create(
                orden=orden,
                producto=item['producto'],
                cantidad=item['cantidad'],
                precio_unitario=item['producto'].precio
            )

        # Vaciar carrito
        request.session['carrito'] = {}

        return render(request, 'checkout_confirmacion.html', {
            'orden': orden,
            'nombre_cliente': nombre_cliente,
            'email_cliente': email_cliente
        })

    return render(request, 'checkout.html', {
        'carrito': productos_carrito, 
        'total': total,
        'user_authenticated': request.user.is_authenticated
    })

def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return render(request, 'detalle_producto.html', {'producto': producto})

# ------------------------------
# Vistas del carrito de compras
# ------------------------------

def agregar_al_carrito(request, producto_id):
    """Agregar producto al carrito usando sesiones"""
    producto = get_object_or_404(Producto, id=producto_id)
    
    # Verificar que hay stock disponible
    if producto.stock <= 0:
        messages.error(request, f'El producto {producto.nombre} no tiene stock disponible.')
        return redirect('productos')
    
    # Obtener carrito de la sesión o crear uno nuevo
    carrito = request.session.get('carrito', {})
    
    # Obtener cantidad del formulario (por defecto 1)
    cantidad = int(request.POST.get('cantidad', 1))
    
    # Verificar que no exceda el stock disponible
    cantidad_actual = carrito.get(str(producto_id), 0)
    if cantidad_actual + cantidad > producto.stock:
        messages.error(request, f'No hay suficiente stock. Stock disponible: {producto.stock}')
        return redirect('productos')
    
    # Agregar o actualizar producto en carrito
    if str(producto_id) in carrito:
        carrito[str(producto_id)] += cantidad
    else:
        carrito[str(producto_id)] = cantidad
    
    # Guardar carrito en sesión
    request.session['carrito'] = carrito
    request.session.modified = True
    
    messages.success(request, f'{producto.nombre} agregado al carrito.')
    return redirect('productos')

def ver_carrito(request):
    """Mostrar contenido del carrito"""
    carrito = request.session.get('carrito', {})
    
    productos_carrito = []
    total = 0
    
    for producto_id, cantidad in carrito.items():
        try:
            producto = Producto.objects.get(id=producto_id)
            subtotal = producto.precio * cantidad
            total += subtotal
            productos_carrito.append({
                'producto': producto,
                'cantidad': cantidad,
                'subtotal': subtotal
            })
        except Producto.DoesNotExist:
            # Eliminar producto que ya no existe
            del carrito[producto_id]
            request.session['carrito'] = carrito
            request.session.modified = True
    
    return render(request, 'carrito.html', {
        'carrito': productos_carrito,
        'total': total
    })

def actualizar_carrito(request, producto_id):
    """Actualizar cantidad de producto en carrito"""
    if request.method == 'POST':
        carrito = request.session.get('carrito', {})
        nueva_cantidad = int(request.POST.get('cantidad', 1))
        
        if nueva_cantidad <= 0:
            # Si la cantidad es 0 o menor, eliminar del carrito
            if str(producto_id) in carrito:
                del carrito[str(producto_id)]
                messages.success(request, 'Producto eliminado del carrito.')
        else:
            # Verificar stock disponible
            producto = get_object_or_404(Producto, id=producto_id)
            if nueva_cantidad > producto.stock:
                messages.error(request, f'No hay suficiente stock. Stock disponible: {producto.stock}')
            else:
                carrito[str(producto_id)] = nueva_cantidad
                messages.success(request, 'Carrito actualizado.')
        
        request.session['carrito'] = carrito
        request.session.modified = True
    
    return redirect('ver_carrito')

def eliminar_del_carrito(request, producto_id):
    """Eliminar producto del carrito"""
    carrito = request.session.get('carrito', {})
    
    if str(producto_id) in carrito:
        producto = get_object_or_404(Producto, id=producto_id)
        del carrito[str(producto_id)]
        request.session['carrito'] = carrito
        request.session.modified = True
        messages.success(request, f'{producto.nombre} eliminado del carrito.')
    
    return redirect('ver_carrito')

def vaciar_carrito(request):
    """Vaciar todo el carrito"""
    request.session['carrito'] = {}
    request.session.modified = True
    messages.success(request, 'Carrito vaciado correctamente.')
    return redirect('ver_carrito')


# ------------------------------
# Vistas de autenticación
# ------------------------------

def registro_usuario(request):
    """Vista para registro de nuevos usuarios"""
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'¡Cuenta creada exitosamente para {username}! Ya puedes iniciar sesión.')
            return redirect('login_usuario')
    else:
        form = RegistroForm()
    
    return render(request, 'registro.html', {'form': form})


def login_usuario(request):
    """Vista para login de usuarios"""
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'¡Bienvenido {username}!')
                # Redirigir a la página anterior o al home
                next_page = request.GET.get('next', 'home')
                return redirect(next_page)
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})


def logout_usuario(request):
    """Vista para logout de usuarios"""
    logout(request)
    messages.success(request, '¡Has cerrado sesión exitosamente!')
    return redirect('home')


@login_required
def perfil_usuario(request):
    """Vista del perfil del usuario con historial de compras"""
    # Obtener órdenes del usuario
    ordenes = OrdenCompra.objects.filter(usuario=request.user).order_by('-fecha')
    
    return render(request, 'perfil.html', {
        'user': request.user,
        'ordenes': ordenes
    })
