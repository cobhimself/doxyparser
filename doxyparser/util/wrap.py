from xml.etree.ElementTree import tostring
from xmlformatter import Formatter

def wrap(text, initial_indent='', subsequent_indent=''):
    lines = text.splitlines()
    begin = initial_indent + lines.pop(0)
    final_lines = []
    for l in lines:
        final_lines.append((subsequent_indent + l) if l.strip() else '')

    return begin + "\n" + "\n".join(final_lines)

def wrapxml(element, initial_indent='', subsequent_indent=''):
    xml = tostring(element, encoding='unicode', method='xml')
    formatter = Formatter(indent=4, selfclose=True, inline=False)
    return wrap(formatter.format_string(xml).decode('UTF-8'))
