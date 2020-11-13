#!/usr/bin/env python3
"""
Model representation of a docRowType from doxygen

<xsd:complexType name="docRowType">
  <xsd:sequence>
    <xsd:element name="entry" type="docEntryType" minOccurs="0" maxOccurs="unbounded" />
  </xsd:sequence>
</xsd:complexType>
"""
from ...node import Node

class DocRow(Node):
  def get_entries(self):
    return self.get_children('entry', 'DocEntry')