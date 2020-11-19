import json
import sys
import pathlib
from xml.etree.ElementTree import ElementTree
from yaml import dump
try:
    from yaml import CDumper as Dumper
except ImportError:
    from yaml import Dumper


class Expectations():
    def __init__(self, tree):
        self._tree = tree

    def generate(self):
        final = self.handle(self._tree.getroot())
        return final

    def handle(self, element):
        is_complex = False
        final = {}
        final[element.tag] = element.attrib
        current = final[element.tag]

        text = '' if element.text is None else element.text.strip()
        tail = '' if element.tail is None else element.tail.strip()
        num_children = len(element)
        if num_children == 0:
            if text != '':
                current['_text'] = text
            if tail != '':
                current['_tail'] = tail
        else:
            if text != '' or tail != '':
                # We have an element that contains text and other elements
                current['_complex'] = [text]
                is_complex = True

            for child in list(element):
                data = self.handle(child)
                if is_complex:
                    # Did we have tail text?
                    tail = data.pop('_tail', None)
                    current['_complex'].append({child.tag: data})
                    if tail is not None:
                        current['_complex'].append(tail)
                else:
                    if (isinstance(current, dict) and child.tag in current.keys()):
                        # We've seen this child tag before...
                        if not isinstance(current[child.tag], list):
                            previous_data = current[child.tag]
                            current[child.tag] = [previous_data]
                        current[child.tag].append(data)
                    else:
                        current[child.tag] = data

        return current


class ExpectationGenerator():
    def __init__(self, xmlfile, output):
        here = str(pathlib.Path(__file__).parent)
        xmldir = here + '/_sample_data/_build/php/xml/'
        ymldir = here + '/_expectation_data/'
        self._xmlfile = xmldir + xmlfile + '.xml'
        self._ymloutput = ymldir + output + '.yml'

    def generate(self):
        tree = ElementTree(file=(self._xmlfile))
        self.write_yml(Expectations(tree).generate())

    def write_yml(self, final):
        stream = open(self._ymloutput, 'w')
        dump(final, stream, Dumper=Dumper, sort_keys=False)


if __name__ == "__main__":
    args = sys.argv
    ExpectationGenerator(args[1], args[2]).generate()
