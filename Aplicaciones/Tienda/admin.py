from django.contrib import admin
from .models import Cliente
from .models import Producto
from .models import Pedido
from .models import DetallePedido
from .models import Categoria

admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(Pedido)
admin.site.register(DetallePedido)
admin.site.register(Categoria)

