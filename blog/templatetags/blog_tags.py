from django import template

register = template.Library()


@register.filter()
def picture_filter(path):
    if path:
        return f"/media/{path}"
    return "#"
