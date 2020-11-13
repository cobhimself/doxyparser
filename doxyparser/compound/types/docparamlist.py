"""
Model representation of a docParamListType from doxygen

<xsd:complexType name="docParamListType">
  <xsd:sequence>
    <xsd:element name="parameteritem" type="docParamListItem" minOccurs="0" maxOccurs="unbounded" />
  </xsd:sequence>
  <xsd:attribute name="kind" type="DoxParamListKind" /> 
</xsd:complexType>
"""
from ...node import Node


class DocParam(Node):
    def get_parameteritems(self):
        return self.get_children('parameteritem', 'DocParamItem')
