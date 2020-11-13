from ...node import Node


class DocTable(Node):
    """
    Model representation of a docTable from doxygen

    <xsd:complexType name="docTableType">
        <xsd:sequence>
            <xsd:element name="caption" type="docCaptionType" minOccurs="0" maxOccurs="1" />
            <xsd:element name="row" type="docRowType" minOccurs="0" maxOccurs="unbounded" />
        </xsd:sequence>
        <xsd:attribute name="rows" type="xsd:integer" />
        <xsd:attribute name="cols" type="xsd:integer" />
    </xsd:complexType>
    """

    def get_caption(self):
        return self.get_child('caption', 'DocCaption')

    def get_rows(self):
        return self.get_children('row', 'DocRow')

    def get_num_rows(self):
        return self.get('rows')

    def get_num_cols(self):
        return self.get('cols')
