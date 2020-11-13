#!/usr/bin/env python3
"""
Model representation of a doxygen element from doxygen's compound.xsd

<xsd:element name="doxygen" type="DoxygenType"/>

<xsd:complexType name="DoxygenType">
  <xsd:sequence maxOccurs="unbounded">
    <xsd:element name="compounddef" type="compounddefType" minOccurs="0" />
  </xsd:sequence>
  <xsd:attribute name="version" type="DoxVersionNumber" use="required" />
  <xsd:attribute ref="xml:lang" use="required"/>
</xsd:complexType>
"""
from ...node import Node

class Doxygen(Node):
    
    def get_compounddefs(self):
      return self.get_children(
        xsd = 'compound',
        tag = 'compounddef'
      )
    
    def get_version(self):
      return self.get('version')