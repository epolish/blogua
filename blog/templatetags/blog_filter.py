from django import template

register = template.Library()

@register.filter
def prepare_search_param(value):
    """Returns prepared GET search param with predefined term"""
    return 'q={}&'.format(value) if value else ''

@register.filter
def add_css_class(field, css):
    """Adds css to fields in templates"""
    return field.as_widget(attrs={"class":css})
