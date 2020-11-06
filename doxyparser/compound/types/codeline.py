#!/usr/bin/env python3
"""
Model representation of a reftext type Element from doxygen

<xsd:complexType name="codelineType">
  <xsd:sequence>
    <xsd:element name="highlight" type="highlightType" minOccurs="0" maxOccurs="unbounded" />
  </xsd:sequence>
  <xsd:attribute name="lineno" type="xsd:integer" />
  <xsd:attribute name="refid" type="xsd:string" />
  <xsd:attribute name="refkind" type="DoxRefKind" />
  <xsd:attribute name="external" type="DoxBool" />
</xsd:complexType>
"""
from ...node import Node

class CodeLine(Node):
    def __init__(self, node):
        super.__init__(node)
    
    def get_highlight(self):
        return self.get_children('highlight', 'Highlight')
    
    def get_lineno(self):
        return self.get('lineno')
    
    def get_ref_id(self):
        return self.get('refid')
    
    def get_ref_kind(self):
        return self.get('refkind')
    
    def get_external(self):
        return self.get_bool('external')