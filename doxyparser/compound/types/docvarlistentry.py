from ...node import Node


class DocVarListEntry(Node):
    """
    Model representation of a docVarListEntryType from doxygen

    <xsd:complexType name="docVarListEntryType">
        <xsd:sequence>
            <xsd:element name="term" type="docTitleType" />
        </xsd:sequence>
    </xsd:complexType>
    """

    def get_term(self):
        return self.get_child('term', 'DocTitle')
