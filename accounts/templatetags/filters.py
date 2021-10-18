from django import template

register = template.Library()

@register.filter(name='zero')
def zero(lista):
    if not lista:
        lista = 0
    else:
        pass

    return lista