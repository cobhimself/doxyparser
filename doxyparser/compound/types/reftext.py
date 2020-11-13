#!/usr/bin/env python3
"""
Model representation of a reftext type Element from doxygen
<xsd:complexType name="refTextType">
  <xsd:simpleContent>
    <xsd:extension base="xsd:string">
     <xsd:attribute name="refid" type="xsd:string" />
     <xsd:attribute name="kindref" type="DoxRefKind" />
     <xsd:attribute name="external" type="xsd:string" use="optional"/>
     <xsd:attribute name="tooltip" type="xsd:string" use="optional"/>
    </xsd:extension>
  </xsd:simpleContent>
</xsd:complexType>
"""
from ...node import Node

class RefText(Node):
    def get_ref_id(self):
        return self.get_text('refid')

    def get_kind_ref(self):
        return self.get('kindref')
    
    def get_external(self):
        return self.get('external')
    
    def get_tooltip(self):
        return self.get('tooltip')