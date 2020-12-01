def wrap(text, initial_indent='', subsequent_indent='      '):
    lines = text.splitlines()
    begin = initial_indent + lines.pop(0)
    return begin + "\n" + "\n".join([subsequent_indent + l for l in lines])