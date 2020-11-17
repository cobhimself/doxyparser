import textwrap
import pprint
import json


class Output():

    def __init__(self, indent_len):
        self._indent_len = indent_len
        self._indent = 0
        self._lines = []
        self._tag_length_cache = {}
        self._wrapper = textwrap.TextWrapper()
        self._wrapper.initial_indent = ''
        self._wrapper.width = 120
        self._wrapper.drop_whitespace = False

    def set_indent(self, indent):
        self._indent = indent

    def inc(self, increase = None):
        increase = self._indent_len if increase is None else increase
        self._indent += increase

    def dec(self, decrease = None):
        decrease = self._indent_len if decrease is None else decrease

        self._indent -= decrease

        if self._indent < 0:
            self._indent = 0

    def puts(self, *args):
        for content in args:
            tag = self.get_formatted_tag(content.pop(0))
            self.add_line(self._indent, tag, content)

    def add_line(self, indent, tag, content):
        if indent not in self._tag_length_cache.keys():
            self._tag_length_cache[indent] = 0

        tag_length = len(tag)
        if tag_length > self._tag_length_cache[indent]:
            self._tag_length_cache[indent] = tag_length

        self._lines.append((indent, tag, content))

    def get_formatted_tag(self, tag):
        return tag

    def get_formatted_content(self, indent, content):
        final = ''
        for i in content:
            if type(i) in (dict, list):
                i = json.dumps(content, indent=2)
            else:
                i = str(i)

            final += i

        return final


    def get_wrapped_line(self, indent, content):
        content = self.get_formatted_content(indent, content)
        additional_indent = self.get_longest_tag_length(indent)
        self._wrapper.subsequent_indent = ' ' * (indent + additional_indent + 2)
        lines = content.splitlines()
        final = ''
        if len(lines) > 0:
            final = lines.pop(0) + "\n"
            for line in lines:
                final += ' ' * (indent + additional_indent + 2) + line + "\n"

        return final.rstrip()

    def dump(self):
        for (indent, tag, content) in self._lines:
            line = self.get_wrapped_line(indent, content)
            indent_str = ' ' * indent
            print(
                '{}{}: {}'.format(
                    indent_str,
                    tag.ljust(self.get_longest_tag_length(indent), ' '),
                    line #"\n".join(line)
                )
            )
        self._lines = []

    def get_longest_tag_length(self, indent):
        return self._tag_length_cache[indent]
