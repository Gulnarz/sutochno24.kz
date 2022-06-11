from django import template

register = template.Library()

@register.filter()
def space(value):
    return '{:,}'.format(value).replace(',', " ")
    
@register.filter()
def apartment(value):
    if value == "О":
        return "Однокомнатная квартира"
    if value == "Д":
        return "Двухкомнатная квартира"