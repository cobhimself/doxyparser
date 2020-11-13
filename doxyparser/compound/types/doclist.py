from ...node import Node


class DocList(Node):
    """
    Model representation of a docListType from doxygen

    <xsd:complexType name="docListType">
        <xsd:sequence>
            <xsd:element name="listitem" type="docListItemType" maxOccurs="unbounded" />
        </xsd:sequence>
    </xsd:complexType>
    """
    def get_listitems(self):
        return self.get_children('listitems', 'DocListItem')
