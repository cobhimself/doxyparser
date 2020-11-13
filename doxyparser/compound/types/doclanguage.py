from ...node import Node


class DocLanguage(Node):
    """
    Model representation of a docLanguageType from doxygen

    <xsd:complexType name="docLanguageType">
        <xsd:sequence>
            <xsd:element name="para" type="docParaType" minOccurs="0" maxOccurs="unbounded" />
        </xsd:sequence>
        <xsd:attribute name="langid" type="xsd:string" />
    </xsd:complexType>
    """

    def get_paras(self):
        return self.get_children('para', 'DocPara')

    def get_langid(self):
        return self.get('langid')
