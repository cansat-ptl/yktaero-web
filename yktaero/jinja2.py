from django.templatetags.static import static
from django.urls import reverse
from django.contrib import messages
from jinja2 import Environment, evalcontextfilter, Markup, escape
import re

    
@evalcontextfilter
def linebreaks(eval_ctx, value):
    """Converts newlines into <p> and <br />s."""
    value = re.sub(r'\r\n|\r|\n', '\n', value) # normalize newlines
    paras = value.replace('\n', '<br />')
    return Markup(paras)


def environment(**options):
    env = Environment(**options)
    env.globals.update({
        'static': static,
        'url': reverse,
        'get_messages': messages.get_messages,
    })
    env.filters['linebreaks'] = linebreaks
    return env