"""
Model representation of a compoundref Element from doxygen

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
from ...node import Node


class CompoundRef(Node):
    def __init__(self, node, parser):
        super.__init__(node, parser, 'compoundref')

    def get_refid(self):
        return self.get('refid', '')

    def get_prot(self):
        return self.get('prot')

    def get_virt(self):
        return self.get('virt')

    def get_fqcn(self):
        return self._node.text
