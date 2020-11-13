"""
Model representation of a docParBlockType from doxygen

<xsd:complexType name="docParBlockType">
  <xsd:sequence>
    <xsd:element name="para" type="docParaType" minOccurs="0" maxOccurs="unbounded" />
  </xsd:sequence>
</xsd:complexType>
"""
from ...node import Node


class DocParBlock(Node):
    def get_paras(self):
        return self.get_children('para', 'docParaType')
