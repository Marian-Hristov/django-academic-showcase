from django import template
register = template.Library()

@register.filter(name='check_permission')
def check_permission(user, permission):
    return user.has_perm(permission)