from django.conf import settings
from django import template
from portfolio.models import Project

register = template.Library()


class LatestProjects(template.Node):
    def __init__(self, limit, varname):
        self.limit = limit
        self.varname = varname

    def render(self, context):
        def resolve_or_not(var, context):
            if callable(getattr(var, 'resolve', None)):
                return var.resolve(context)
            return var

        limit = resolve_or_not(self.limit, context)
        varname = resolve_or_not(self.varname, context)

        context[varname] = Project.active.order_by('-id')[:int(limit)]
        return u''


@register.tag
def get_latest_projects(parser, token):
    ''' Returns the latest projects stored in the db.

        {% get_latest_projects 5 as "projects" %}

        Will return the last 5 projects and store in the 
        template context as "projects"..
    '''
    bits = token.split_contents()
    if len(bits) != 4:
        raise template.TemplateSyntaxError(
            '"%s" tag takes exactly 3 arguments' % bits[0]
        )

    _tag, limit, _as, varname = bits

    return LatestProjects(
        parser.compile_filter(limit),
        parser.compile_filter(varname),
    )


def split(value, splitter):
    return value.split(splitter)

register.filter('split', split)
