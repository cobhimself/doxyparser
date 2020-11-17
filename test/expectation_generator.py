import sys
import pathlib
from xml.etree.ElementTree import XMLParser
from yaml import dump
try:
    from yaml import CDumper as Dumper
except ImportError:
    from yaml import Dumper

class ExpectParser():
    final = {}
    current_tag = {}
    prev_tag = {}
    depth = 0
    stack = []

    def start(self, tag, attrib):   # Called for each opening tag.
        self.depth += 1
        self.add_tag(tag)
        self.set_attr(attrib)

    def end(self, tag):             # Called for each closing tag.
        self.depth -= 1
        self.stack = self.stack[:-1]

    def data(self, data):
        ref = self.get_current_data_ref()
        data = data.strip()
        if data != '':
            ref['_text'] = data

    def close(self):
        return self.get_final()


    def set_attr(self, attributes):
        data_ref = self.get_current_data_ref()
        print('setting attributes')
        for attr, value in attributes.items():
            data_ref[attr] = value

    def get_final(self):
        return self.final

    def add_tag(self, tag):
        print('Adding tag: ', tag)
        start = self.get_current_data_ref()
        # Have we seen this tag before?
        # If so, we need an array of tags, not a dict
        if type(start) is dict and tag in start.keys():
            print('-- seeing tag again, making it an array')
            # Our data should be an array now, fill it with
            # our previous data
            print('-- before: ', start[tag])
            if type(start[tag]) is dict:
                start[tag] = [start[tag]]
                print('-- after: ', start[tag])

            length = len(start[tag])
            print('-- new length: ', length)
            start[tag].append({})
            print('-- final: ', start[tag])
            self.stack.append(start[tag][length])
        elif type(start) is list:
            print('-- we have a list for ' + tag)
            length = len(start[tag])
            start[tag][length] = {}
            print('new list for ' + tag + ': ', start[tag][length])
            self.stack.append(start[tag][length])
        else:
            print('-- new tag dictionary')
            start[tag] = {}
            self.stack.append(start[tag])

    def get_current_data_ref(self):
        if len(self.stack) == 0:
            print('Returning final ref')
            return self.final
        else:
            print('Current ref: ', self.stack[-1])
            return self.stack[-1]

class ExpectationGenerator():
    def __init__(self, xmlfile, output):
        here = str(pathlib.Path(__file__).parent)
        xmldir =  here + '/_sample_data/_build/php/xml/'
        ymldir = here + '/_expectation_data/'
        self._xmlfile = xmldir + xmlfile + '.xml'
        self._ymloutput = ymldir + output + '.yml'

    def generate(self, node=None):
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
