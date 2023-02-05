from django import template

register = template.Library()

@register.filter
def truncate(value, length):
    if len(value) > length:
        return value[:length] + '...'
    return value
