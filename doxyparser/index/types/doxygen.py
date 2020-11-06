#!/usr/bin/env python3
"""
Model representation of a DoxygenType Element from doxygen

<xsd:complexType name="DoxygenType">
  <xsd:sequence>
    <xsd:element name="compound" type="CompoundType" minOccurs="0" maxOccurs="unbounded"/>
  </xsd:sequence>
  <xsd:attribute name="version" type="xsd:string" use="required"/>
  <xsd:attribute ref="xml:lang" use="required"/>
</xsd:complexType>
"""
from ...node import Node

class Doxygen(Node):
  def __init__(self, node):
    super.__init__(node)
  
  def get_compounds(self):
    return self.get_children('compound', 'Compound')
  
  def get_version(self):
    return self.get('version')
  
  def get_ref(self):
    return self.get('ref')