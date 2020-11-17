from ...node import Node


class Ref(Node):
    """
    Model representation of a refType Element from doxygen

    <xsd:complexType name="refType">
    <xsd:simpleContent>
        <xsd:extension base="xsd:string">
        <xsd:attribute name="refid" type="xsd:string" />
        <xsd:attribute name="prot" type="DoxProtectionKind" use="optional"/>
        <xsd:attribute name="inline" type="DoxBool" use="optional"/>
        </xsd:extension>
    </xsd:simpleContent>
    </xsd:complexType>
    """
    def get_refid(self):
        return self.get('refid')

    def get_prot(self):
        return self.get('prot', '')

    def is_inline(self):
        return self.get_bool('inline')
