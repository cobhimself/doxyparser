#!/usr/bin/env python3
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
from ...node import Node

class Ref(Node):
    def get_ref_id(self):
        return self.get_text('refid')
    
    def get_prot(self):
        return self.get_text('prot', '')
    
    def is_inline(self):
        return self.get_bool('inline')