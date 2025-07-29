from django import template
from django.template import Context, Template as DjangoTemplate, TemplateSyntaxError as DjangoTemplateSyntaxError
from django.template.base import VariableDoesNotExist

register = template.Library()

MAX_CACHE = 100
django_cache = {}


def compile_template(code):
    if code in django_cache:
        return django_cache[code]

    # If this works for re.compile, it works for us too.
    if len(django_cache) > MAX_CACHE:
        django_cache.clear()

    t = django_cache[code] = DjangoTemplate(code)
    return t


@register.simple_tag(takes_context=True)
def render_django_tag(context, template, **kwargs):
    try:
        # Merge context with additional kwargs
        render_context = context.flatten()
        render_context.update(kwargs)
        return compile_template(template).render(Context(render_context))
    except (VariableDoesNotExist, DjangoTemplateSyntaxError):
        return 'Error rendering: %r' % template 