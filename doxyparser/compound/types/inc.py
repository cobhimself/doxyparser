"""
Model representation of a incType Element from doxygen

<xsd:complexType name="incType">
<xsd:simpleContent>
    <xsd:extension base="xsd:string">
    <xsd:attribute name="refid" type="xsd:string" />
    <xsd:attribute name="local" type="DoxBool" />
    </xsd:extension>
</xsd:simpleContent>
</xsd:complexType>
"""
from ...node import Node


class Inc(Node):
    def get_ref_id(self):
        return self.get('refid')

    def is_local(self):
        return self.get_bool('local')
