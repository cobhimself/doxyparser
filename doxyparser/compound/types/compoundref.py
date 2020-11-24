from ...node import Node


class CompoundRefType(Node):
    """
    Model representation of a compoundrefType from doxygen

    <xsd:complexType name="compoundRefType">
        <xsd:simpleContent>
            <xsd:extension base="xsd:string">
                <xsd:attribute name="refid" type="xsd:string" use="optional" />
                <xsd:attribute name="prot" type="DoxProtectionKind" />
                <xsd:attribute name="virt" type="DoxVirtualKind" />
          </xsd:extension>
        </xsd:simpleContent>
    </xsd:complexType>

    """

    def get_refid(self):
        return self.get('refid', '')

    def get_prot(self):
        return self.get('prot')

    def get_virt(self):
        return self.get('virt')

    def get_fqcn(self):
        return self._node.text
