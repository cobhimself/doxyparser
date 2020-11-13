#!/usr/bin/env python3
"""
Model representation of a docindexentry type from doxygen

<xsd:complexType name="docIndexEntryType">
  <xsd:sequence>
    <xsd:element name="primaryie" type="xsd:string" />
    <xsd:element name="secondaryie" type="xsd:string" />
  </xsd:sequence>
</xsd:complexType>
"""
from ...node import Node

class DocIndexEntry(Node):
  
  def get_primaryie(self):
    return self.get_text('primaryie')
  
  def get_secondaryie(self):
    return self.get_text('secondaryie')