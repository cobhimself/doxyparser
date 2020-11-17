class Parser:
    """Main doxyparser Parser class.
    """
    def __init__(self, loader):
        self._loader = loader

    def parse_index(self):
        """
            Parse the index.xml file associated with this parser's loader's
            build directory.

        Returns:
            doxyparser.index.types.DoxygenIndex
        """
        tree = self._loader.load_index()
        return self.get_node_from_tree(
            'index',
            tree
        )

    def parse_ref_id(self, refid, xsd='compound'):
        """
            Parse the data in the file associated with the refid.

        Args:
            refid (string): The refid to load.
            xsd (str, optional): The xsd folder name the model the root
                element will relate to. Defaults to 'compound'.

        Returns:
            doxyparser.compound.types.Doxygen: The Doxygen model associated
                with the refid data.
        """
        tree = self._loader.load_refid(refid)
        return self.get_node_from_tree(
            xsd,
            tree
        )

    def get_tag_class(self, xsd, tag):
        """Get the class associated with the given xsd and tag.

        Args:
            xsd (string): The xsd where this tag class lives.
            tag (string): The tag whose doxyparser class should be
            returned for.

        Returns:
            Module: The class associated with the given xsd and tag.
        """
        return self._loader.load_tag_class(xsd, tag)

    def get_tag_class_instance(self, xsd, tag, element, tree):
        """Retrieve an instance of the doxyparser class this tag relates to.

        Args:
            xsd (string): The xsd where the doxyparser class lives.
            tag (string): The tag to obtain the doxparser class
            instance from.
            element (xml.etree.Element): The Element whose data will be given
                to the doxyparser model.
            tree (doxyparser.tree.Tree): The tree this doxyparser model
                should reference when obtaining the data source.

        Returns:
            Node: The doxyparser Node model associated with the given xsd
                and tag.
        """
        tag = self.get_tag_class(xsd, tag)
        return tag(element, self, tree)

    def get_node_from_tree(self, xsd, tree):
        """
            Get the doxyparser model associated with the root tag in the
            given tree.

        Args:
            xsd (string): The xsd folder where the doxyparser element can
                be found.
            tree (doxyparser.tree.Tree): The Tree to obtain data from.

        Returns:
            [type]: [description]
        """
        root = tree.get_parsed()

        return self.get_tag_class_instance(xsd, root.tag, root, tree)
