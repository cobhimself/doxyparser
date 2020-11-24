from doxyparser import TAG_MAP
from importlib import import_module
from .tree import Tree


class Loader():
    """Class responsible for loading xml files and classes relating to nodes
    """

    cache = {}

    def __init__(self, xml_dir):
        self._xml_dir = xml_dir

    def load_index(self):
        """Return the Tree associated with the index.xml file.

        Returns:
            Tree: The tree with the data from index.xml
        """
        return self.load('index')

    def load(self, file):
        return Tree().parse(self._xml_dir + '/' + file + '.xml')

    @staticmethod
    def load_tag_class(xsd, tag):
        """
        Load the given doxyparser class associated with the given xsd
        and tag.

        Args:
            xsd (string): The xsd folder where the tag class can be found.
            tag (string): The tag whos doxyparser model should be loaded.

        Raises:
            Exception: If the given xsd cannot be found.
            Exception: If no class mapping exists for the given tag.

        Returns:
            class: The doxyparser class for the given xsd and tag.
        """
        if (xsd, tag) not in Loader.cache:

            if xsd not in TAG_MAP.keys():
                raise Exception(
                    'Unable to load tag class with xsd "' + xsd + '", '
                    + 'tag: "' + tag + '". Check TAG_MAP in doxyparser/__init__.py'
                )

            if tag not in TAG_MAP[xsd].keys():
                raise Exception(
                    'No class mapping for tag ' + tag + ' is set! Update doxyparser/__init__.py'
                )

            path = TAG_MAP[xsd][tag]
            parts = path.split('.')
            final = parts.pop()
            package = '.'.join(parts)

            module = import_module(package)

            Loader.cache[(xsd, tag)] = getattr(module, final)

        return Loader.cache[(xsd, tag)]

    def load_refid(self, refid):
        """Load the Tree for the given refid

        Args:
            refid (string): The refid file to load (minus .xml)

        Returns:
            Tree: The tree for the refid xml file.
        """
        return self.load(refid)
