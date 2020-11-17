"""
An extension of xml.etree.ElementTree
"""
from xml.etree.ElementTree import ElementTree


class Tree(ElementTree):
    """
    An extension of xml.etree.ElementTree with the ability to save the source
    file information.
    """

    def get_source(self):
        """Return the source file name where this tree was obtained.

        Returns:
            string: The file name where this tree was obtained.
        """
        return self._source

    def get_parsed(self):
        return self._parsed

    def parse(self, source, parser=None):
        """Load external XML document into element tree.

        Args:
            source (mixed): a file name or file object
            parser: is an optional parser instance that defaults
            to XMLParser.

        Raises:
            ParseError: if the parser fails to parse the document.

        Returns:
            xml.etree.Element: the root element of the given source document.
        """
        self._source = source
        self._parsed = super().parse(source, parser)

        return self
