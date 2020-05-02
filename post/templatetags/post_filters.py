from django import template
from django.template.defaultfilters import stringfilter
from django.utils.html import mark_safe,format_html
register = template.Library()

@register.filter(name='tagize')
@stringfilter
def tagize(value):
    value = value.replace('<p>',' <p> ')
    value = value.replace('<br>',' <br> ')
    value = value.replace('</p>',' </p> ')
    tokens = value.split(' ')
    output = ""
    for token in tokens:
        try:
            if token[0]=='@' and len(token)>3 and len(token)<22:
                valid = True
                for ch in token[1:]:
                    if ch!='.' and ch!='_' and not ch.isalpha() and not ch.isdigit():
                        valid = False
                        break
                if valid:
                    output += '<a class="tag-link" href="/users/'+ token[1:] +'/">' + token + '</a> '
                else:
                    output += token + ' '
            else:
                output += token + ' '
        except:
            output += token + ' '
    format_html(output)
    return output[:-1]