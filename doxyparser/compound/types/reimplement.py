"""
Model representation of a reimplement type from doxygen

<xsd:complexType name="reimplementType">
  <xsd:simpleContent>
    <xsd:extension base="xsd:string">
      <xsd:attribute name="refid" type="xsd:string" />
    </xsd:extension>
  </xsd:simpleContent>
</xsd:complexType>
"""
from ...node import Node


class Reimplement(Node):
    def get_ref_id(self):
        return self.get('refid')
