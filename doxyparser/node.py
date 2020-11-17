class Node:
    """
    Super class used to represent doxy xml Elements
    """

    def __init__(self, node, parser, tree, tag=None):
        """
        Initialize a Node (object representation of an xml data tree)

        Args:
            node (xml.etree.ElementTree.Element): The Element this
                Node references
            parser (doxyparser.parser): The parser for this node.
            tree (doxyparser.tree): The tree this node originated.
            tag (string, optional): The tag this node represents. If
                provided, a check is made to to confirm.
                Defaults to None.

        Raises:
            Exception: Raised if a tag name is provided and it doesn't
                match with the Element's tag
        """
        if parser is None:
            raise Exception(
                'The node class cannot be instantiated without a parser!'
            )

        if tag not in (None, node.tag):
            raise Exception(
                'Invalid tag name ('
                + node.tag
                + '). Expected '
                + tag
            )

        self._node = node
        self._child_cache = {}
        self._parser = parser
        self._xsd = self.__module__.split('.')[1]
        self._origin_tree = tree

    def __len__(self):
        return len(self._node)

    def get(self, attribute, default=None):
        """Get the value of the given attribute of this element.

        Args:
            attribute (string): The attribute name
            default (mixed, optional): The value to use if the attribute has
               no value. Defaults to None.

        Returns:
            string: the value of the attribute
        """
        return self._node.get(attribute, default)

    def find(self, key, default=None):
        """Finds the first subelement matching match.

        Args:
            key (string): may be a tag name or path
            default (mixed, optional): the default return value if key
                is not found. Defaults to None.

        Returns:
            Element|None: Returns an Element instance or none if
                not found
        """
        child = self._node.find(key)

        if child is None:
            return default

        return child

    def get_text(self, key, default=None):
        """Get the text from the first element matching key.

        Args:
            key (string): May be a tag name or path
            default (mixed, optional): Returned if key not found. Defaults to None.

        Returns:
            string|mixed: If the Element with key is found, its text is
                returned. Otherwise the default.
        """
        found = self.find(key)
        if found is None:
            return default
        else:
            return found.text

    def iter(self, tag):
        """Iterate over the child elements matching the given tag.

        Args:
            tag (string): The tag to iterate

        Returns:
            iterator: An iterator for all child elements matching the
            given tag.
        """
        return self._node.iterfind(tag)

    def get_bool(self, attr):
        """Get the boolean value of an attribute on this element.

        Args:
            attr (string): The name of the attribute to return a boolean
                value for.

        Returns:
            bool: The boolean value of the attribute
        """
        value = self.get(attr)
        return value == 'yes'

    def get_children(self, tag, xsd=None, path=None):
        """Get the children elements at the given tag as models.

        Args:
            tag (string): The tag of the child elements you want to get.
            xsd (string, optional): The xsd name this element's model class
                lives within. Defaults to the classes' parent xsd
                folder name.
            path (string, optional): The xpath to apply to the search.
                Defaults to None.

        Returns:
            list: Returns a list of doxparser type classes based on the tag
                and, optionally, xsd.
        """
        xsd = self._xsd if xsd is None else xsd

        xpath = tag + ('' if path is None else path)
        if xpath not in self._child_cache.keys():
            child_class = self._parser.get_tag_class(xsd, tag)

            children = []
            for child in self.iter(xpath):
                children.append(child_class(child, self._parser, self._origin_tree))

            self._child_cache[xpath] = children

        return self._child_cache[xpath]

    def get_child(self, tag, xsd=None, path=None):
        """Get the first child element of this element with the given tag name.

        Args:
            tag (string): The tag of the child elements you want to get.
            xsd (string, optional): The xsd name this element's model class
                lives within. Defaults to the classes' parent xsd
                folder name.
            path (string, optional): The xpath to apply to the search.
                Defaults to None.

        Returns:
            Node: The child Node class for the given tag.
        """
        xsd = self._xsd if xsd is None else xsd
        children = self.get_children(tag, xsd, path)
        if children is not None:
            return children[0]

        return None

    def debug_dump(self):
        """Dump data about this element.
        """
        self._node.dump()

    def parse_ref(self, xsd, refid):
        """
            Parse and return an instance of the doxyparser model for the xml
            document relating to the given refid.

        Args:
            xsd (string): The xsd where the refid lives.
            refid (string): The refid to load

        Returns:
            : [description]
        """
        return self._parser.parse_ref_id(xsd, refid)

    def get_source_file(self):
        """Get the source file where the data for this node originates.

        Returns:
            string: The file where this data originated
        """
        return self._origin_tree.get_source()

    def __str__(self):
        return self.__module__ + ': ' + self._origin_tree.get_source()

    def __rep__(self):
        return self.__str__()
