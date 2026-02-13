from django import template
register = template.Library()

@register.filter
def attr(obj, name: str):
    if obj is None:
        return ""
    return getattr(obj, name, "")
