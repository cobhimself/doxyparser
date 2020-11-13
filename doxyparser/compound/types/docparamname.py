"""
Model representation of a docParamName from doxygen

<xsd:complexType name="docParamName" mixed="true">
  <xsd:sequence>
    <xsd:element name="ref" type="refTextType" minOccurs="0" maxOccurs="1" />
  </xsd:sequence>
  <xsd:attribute name="direction" type="DoxParamDir" use="optional" />
</xsd:complexType>
"""
from ...node import Node


class DocParamName(Node):
    def get_ref(self):
        return self.get_child('ref', 'RefText')

    def get_direction(self):
        return self.get('direction')
