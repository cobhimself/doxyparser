#!/usr/bin/env python3
"""
Model representation of a MemberType Element from doxygen

<xsd:complexType name="MemberType">
  <xsd:sequence>
    <xsd:element name="name" type="xsd:string"/>
  </xsd:sequence>
  <xsd:attribute name="refid" type="xsd:string" use="required"/>
  <xsd:attribute name="kind" type="MemberKind" use="required"/>
</xsd:complexType>
"""
from ...node import Node

class Member(Node):
  def __init__(self, node):
    super().__init__(node)
  
  def get_name(self):
    return self.get_text('name')
  
  def get_refid(self):
    return self.get('refid')
  
  def get_kind(self):
    return self.get('kind')