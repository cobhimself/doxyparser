from ...node import Node


class DocBlockQuote(Node):
    """
    Model representation of a docblockquote type Element from doxygen

    <xsd:complexType name="docBlockQuoteType">
        <xsd:sequence>
            <xsd:element name="para" type="docParaType" minOccurs="0" maxOccurs="unbounded" />
        </xsd:sequence>
    </xsd:complexType>
    """

    def get_paras(self):
        return self.get_children('para', 'DocPara')
