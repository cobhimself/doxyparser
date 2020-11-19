import json
import sys
import pathlib
from xml.etree.ElementTree import XMLParser
from yaml import dump
try:
    from yaml import CDumper as Dumper
except ImportError:
    from yaml import Dumper

class ExpectStack():
    final = {}
    pointer = ''
    depth = 0
    content_depth = 0
    content_buffer = []
    content_pointer = None
    stack = []

    def add(self, ref, tag=None):
        if tag is not None:
            print('Adding tag', tag)
            self.dive(tag)
        self.stack.append(ref)

    def pop(self, rise=True):
        print('Moving up a reference')
        self.stack = self.stack[:-1]
        if rise:
            self.rise()

    def current(self):
        if len(self.stack) == 0:
            return self.final

        return self.stack[-1]

    def dive(self, tag):
        self.pointer += ('' if self.pointer == '' else '.') + tag
        print('Dive: ' + self.pointer)

    def rise(self):
        self.pointer = self.pointer.rpartition('.')[0]
        print('Rise: ' + self.pointer)

    def buffer_len(self):
        return len(self.content_buffer)

    def buffer(self):
        return self.content_buffer

    def set_buffer(self, content):
        self.content_buffer = content

    def dump_buffer(self):
        final = self.content_buffer[:]
        self.content_buffer = []
        self.content_pointer = None

        print('Dumping buffer: ', final)
        return final

    def set_buffer_pointer(self, pointer):
        print('New buffer pointer:', pointer)
        self.content_pointer = pointer

    def buffer_is_only_str(self):
        return self.buffer_len() == 1 and isinstance(self.buffer()[0], str)

    def sync_buffer_pointer(self):
        print('Syncing buffer pointer')
        self.set_buffer_pointer(self.pointer)

    def append_buffer(self, data):
        print('Adding to buffer:', data)
        self.content_buffer.append(data)

    def at_buffer_start_point(self):
        return self.pointer == self.content_pointer

class Expectations():
    final = {}
    current_tag = ''
    prev_tag = {}
    stack = ExpectStack()
    content_nodes = [
        'para'
    ]
    pause_parsing = False

    def add_tag(self, tag):
        self.current_tag = tag
        start = self.stack.current()
        if self.pause_parsing:
            start.append({tag: {}})
            self.stack.add(start[len(start)-1][tag], tag)
        # Have we seen this tag before?
        # If so, we need an array of tags, not a dict
        elif isinstance(start, dict) and tag in start.keys():
            # Our data should be an array now, fill it with
            # our previous data
            if isinstance(start[tag], dict):
                start[tag] = [start[tag]]

            length = len(start[tag])
            start[tag].append({})
            self.stack.add(start[tag][length], tag)
        elif isinstance(start, list):
            length = len(start[tag])
            start[tag][length] = {}
            self.stack.add(start[tag][length], tag)
        else:
            start[tag] = {}
            self.stack.add(start[tag], tag)

    def lines_from_complex(self, content):
        pass

    def set_attr(self, attributes):
        # Get the data reference of the tag we just added
        data_ref = self.stack.current()
        for attr, value in attributes.items():
            data_ref[attr] = value

    def get_final(self):
        return self.final


    def add(self, tag, attrib):
        if self.pause_parsing:
            # Add any new data to our content buffer
            self.stack.add(self.stack.buffer())
            # Add a tag to our content buffer
            self.add_tag(tag)
            # Set the attributes for the tag in our content buffer
            self.set_attr(attrib)
            # We no longer want to reference our content buffer, move a level
            # up
            self.stack.pop()
        else:
            # Add a tag to our current expectations
            self.add_tag(tag)
            # Set the tag attributes
            self.set_attr(attrib)

    def end(self, tag):
        if (self.stack.at_buffer_start_point()):
            self.pause_parsing = False
            self.stack.pop(False)
            ref = self.stack.current()
            if self.stack.buffer_is_only_str():
                self.stack.set_buffer(self.stack.buffer()[0].strip())
                key = '_text'
            else:
                key = '_complex'

            ref[tag][key] = self.stack.dump_buffer()

        self.stack.pop()

    def data(self, data):
        self.stack.sync_buffer_pointer()

        data = data.lstrip()
        if data != '':
            self.stack.append_buffer(data)
            self.pause_parsing = True

    def finalize(self, root=None):
        return self.get_final()
        root = self.final if root is None else root
        for tag, data in root.items():
            if tag == '_complex':
                lines = self.lines_from_complex(data)
                root[tag]['_lines'] = lines
            elif isinstance(data, dict):
                self.finalize(data)

class ExpectParser():
    expectations = Expectations()

    def start(self, tag, attrib):   # Called for each opening tag.
        self.expectations.add(tag, attrib)

    def end(self, tag):             # Called for each closing tag.
        self.expectations.end(tag)

    def data(self, data):
        self.expectations.data(data)

    def close(self):
        return self.expectations.finalize()



class ExpectationGenerator():
    def __init__(self, xmlfile, output):
        here = str(pathlib.Path(__file__).parent)
        xmldir =  here + '/_sample_data/_build/php/xml/'
        ymldir = here + '/_expectation_data/'
        self._xmlfile = xmldir + xmlfile + '.xml'
        self._ymloutput = ymldir + output + '.yml'

    def generate(self):
        target = ExpectParser()
        parser = XMLParser(target=target)
        parser.feed(open(self._xmlfile, 'r').read())

        self.write_yml(parser.close())

    def write_yml(self, final):
        stream = open(self._ymloutput, 'w')
        dump(final, stream, Dumper=Dumper, sort_keys=False)


if __name__ == "__main__":
    args = sys.argv
    ExpectationGenerator(args[1], args[2]).generate()
