from django import template
register = template.Library()

# pagina 188 numerada - 203 del libro
def completar(comp):
    if len(comp)<8:
        mod="0"*(8-len(comp)) +comp
        return mod
    else:
        return comp

register.filter('completar', completar)