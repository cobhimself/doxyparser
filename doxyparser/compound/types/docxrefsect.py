#!/usr/bin/env python3
"""
Model representation of a docXRefSectType from doxygen

<xsd:complexType name="docXRefSectType">
  <xsd:sequence>
    <xsd:element name="xreftitle" type="xsd:string" minOccurs="0" maxOccurs="unbounded" />
    <xsd:element name="xrefdescription" type="descriptionType" />
  </xsd:sequence>
  <xsd:attribute name="id" type="xsd:string" /> 
</xsd:complexType>
"""
from ...node import Node

class DocXRefSect(Node):
  def __init__(self, node):
      super.__init__(node)
  
  def get_xreftitle(self):
    return self.get_text('xreftitle')
  
  def get_xrefdescription(self):
    return self.get_child('xrefdescription', 'Description')
  
  def get_id(self):
    return self.get('id')