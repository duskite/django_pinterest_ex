import markdown
from django.utils.safestring import mark_safe
from django import template

register = template.Library()

@register.filter
def mark(value):
    extentions = ['nl2br', 'fenced_code']
    return mark_safe(markdown.markdown(value, extensions=extentions))


