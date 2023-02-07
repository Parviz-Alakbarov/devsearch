from django import template

register = template.Library()

@register.filter
def truncate(value, length):
    if value is None:
        return ''
    if len(value) > length:
        return value[:length] + '...'
    return value
