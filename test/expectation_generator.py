import sys
import pathlib
from xml.etree.ElementTree import Element
from yaml import dump
try:
    from yaml import CDumper as Dumper
except ImportError:
    from yaml import Dumper

from doxyparser.loader import Loader
from doxyparser.parser import Parser
from doxyparser.decorators import COLLECTORS

class ModelData():
    cache = {}
    def __init__(self, xsd, parser, tree):
        self._xsd = xsd
        self._parser = parser
        self._empty_element = Element('blank')
        self._tree = tree

    def get_model_collections(self, tag):
        if tag not in self.cache.keys():
            model = self._parser.get_tag_class_instance(
                self._xsd,
                tag,
                self._empty_element,
                self._tree
            )
            self.cache[tag] = model

        collections = self.cache[tag].get_collections()
        return collections if None is not collections else {}



class Expectations():

    attr_value_map = {
        'no': False,
        'yes': True
    }

    attr_key_map = {
        'bodyfile': 'body_file',
        'bodystart': 'body_start',
        'bodyend': 'body_end',
        'refid': 'ref_id',
        'kindref': 'kind_ref',
    }

    element_key_map = {
        'sectiondef': 'section_defs',
        'memberdef': 'member_def',
        'argsstring': 'args_string',
        'inbodydescription': 'in_body_description',
        'detaileddescription': 'detailed_description',
        'briefdescription': 'brief_description',
        'basecompoundref': 'base_compound_ref',
        'compoundname': 'compound_name',
        'compounddef': 'compound_defs',
        'childnode': 'child_node',
        'collaborationgraph': 'collaboration_graph',
    }

    def __init__(self, tree):
        self._tree = tree
        self._xsd = None
        self._model_data = None

    def generate(self, xsd, parser):
        self._xsd = xsd
        self._model_data = ModelData(xsd, parser, self._tree)
        final = self.handle(self._tree.getroot())
        return final

    def handle_attr(self, attributes):
        final = {}
        for key, value in attributes.items():
            if key in self.attr_key_map.keys():
                key = self.attr_key_map[key]

            if value in self.attr_value_map.keys():
                value = self.attr_value_map[value]

            final[key] = value

        return final

    def handle_tag(self, tag):
        if tag in self.element_key_map.keys():
            return self.element_key_map[tag]

        return tag

    def handle(self, element):
        is_complex = False
        final = {}
        tag = self.handle_tag(element.tag)
        final[tag] = self.handle_attr(element.attrib)
        current = final[tag]

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


            if not self.handle_collection(current, element, is_complex):
                for child in list(element):
                    data = self.handle(child)
                    child_tag = self.handle_tag(child.tag)
                    if is_complex:
                        # Did we have tail text?
                        tail = data.pop('_tail', None)
                        current['_complex'].append({child_tag: data})
                        if tail is not None:
                            current['_complex'].append(tail)
                    else:
                        if (isinstance(current, dict) and child_tag in current.keys()):
                            # We've seen this child tag before...
                            if not isinstance(current[child_tag], list):
                                previous_data = current[child_tag]
                                current[child_tag] = [previous_data]
                            current[child_tag].append(data)
                        else:
                            current[child_tag] = data

        return current

    def handle_collector(self, getter, elem_filter, element, current, is_complex):
        matching_elements = element.findall(elem_filter)

        if len(matching_elements) > 0:
            current[getter] = {'count': len(matching_elements)}
            current[getter]['expectations'] = {}

        for child in matching_elements:
            child_data = self.handle(child)
            child_tag = self.handle_tag(child.tag)
            expectations = current[getter]['expectations']
            if is_complex:
                # Did we have tail text?
                tail = child_data.pop('_tail', None)
                current['_complex'].append({child_tag: child_data})
                if tail is not None:
                    current['_complex'].append(tail)
            else:
                if (isinstance(expectations, dict) and child_tag in expectations.keys()):
                    # We've seen this child tag before...
                    if not isinstance(expectations[child_tag], list):
                        previous_data = expectations[child_tag]
                        expectations[child_tag] = [previous_data]
                    expectations[child_tag].append(child_data)
                else:
                    expectations[child_tag] = child_data

    def handle_collection(self, current, element, is_complex):
        collection_data = self._model_data.get_model_collections(element.tag)
        if len(collection_data) == 0:
            return False

        for collection_tag, data in collection_data.items():
            #The tag associated with the collection will have a method whose
            #name will be the plural form of the element tag and it will
            #return all of the elements for the tag name.
            getter = collection_tag + 's'
            self.handle_collector(getter, collection_tag, element, current, is_complex)

            xpath_template = data['path']
            for collector, xpath_args in data[COLLECTORS].items():
                xpath = xpath_template.format(**xpath_args)
                xpath = '{}{}'.format(collection_tag, xpath)
                getter = collection_tag + '_' + collector
                self.handle_collector(getter, xpath, element, current, is_complex)

        return True


class ExpectationGenerator():
    def __init__(self, xmlfile, output):
        here = str(pathlib.Path(__file__).parent)
        xmldir = here + '/_sample_data/_build/php/xml/'
        ymldir = here + '/_expectation_data/'
        self._xmlfile = xmlfile
        self._ymloutput = ymldir + output + '.yml'
        self._parser = Parser(Loader(xmldir))
        self._xsd = 'index' if self._xmlfile.endswith('index') else 'compound'

    def generate(self):
        tree = self._parser.get_loader().load(self._xmlfile)
        self.write_yml(Expectations(tree).generate(self._xsd, self._parser))

    def write_yml(self, final):
        stream = open(self._ymloutput, 'w')
        dump(final, stream, Dumper=Dumper, sort_keys=False)


if __name__ == "__main__":
    args = sys.argv
    ExpectationGenerator(args[1], args[2]).generate()
