"""
Model representation of a spType Element from doxygen

<xsd:complexType name="spType" mixed="true">
  <xsd:attribute name="value" type="xsd:integer" use="optional"/>
</xsd:complexType>
"""
from ...node import Node


class Sp(Node):
    def get_value(self):
        return self.get('value')
