from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    """Multiplica value por arg."""
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError):
        return 0

@register.simple_tag
def calcular_total(carrito):
    """Suma todos los subtotales del carrito."""
    total = 0
    for item in carrito:
        try:
            # Si item es un diccionario (como en checkout)
            if isinstance(item, dict):
                total += float(item['producto'].precio) * float(item['cantidad'])
            # Si item es un objeto con atributos (para compatibilidad futura)
            else:
                total += float(item.producto.precio) * float(item.cantidad)
        except (ValueError, TypeError, KeyError):
            pass
    return total

