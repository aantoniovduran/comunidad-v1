from django import template
from pagos.models import Pagos

register = template.Library()

@register.simple_tag
def pagos_counter():
    return Pagos.objects.count()


@register.inclusion_tag('pagina/pagos.html')
def listapagos1():
    return {
        'paglist' : Pagos.objects.all()
    }
