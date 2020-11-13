#!/usr/bin/env python3
"""
Model representation of a docParamNameList from doxygen

<xsd:complexType name="docParamNameList">
  <xsd:sequence>
    <xsd:element name="parametertype" type="docParamType" minOccurs="0" maxOccurs="unbounded" />
    <xsd:element name="parametername" type="docParamName" minOccurs="0" maxOccurs="unbounded" />
  </xsd:sequence>
</xsd:complexType>
"""
from ...node import Node

class DocParamNameList(Node):
  def get_parametertypes(self):
    return self.get_children('parametertype', 'DocParam')

  def get_parameternames(self):
    return self.get_children('parametername', 'DocParamName')