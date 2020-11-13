from ...node import Node


class DocTocList(Node):
    """
    Model representation of a docTocListType from doxygen

    <xsd:complexType name="docTocListType">
        <xsd:sequence>
            <xsd:element name="tocitem" type="docTocItemType" minOccurs="0" maxOccurs="unbounded" />
        </xsd:sequence>
    </xsd:complexType>
    """

    def get_tocitems(self):
        return self.get_children('tocitem', 'DocTocItem')
