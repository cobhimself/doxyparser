#!/usr/bin/env python3
"""
Model representation of a docParamListItem from doxygen

<xsd:complexType name="docParamListItem">
<xsd:sequence>
  <xsd:element name="parameternamelist" type="docParamNameList" minOccurs="0" maxOccurs="unbounded" />
  <xsd:element name="parameterdescription" type="descriptionType" />
</xsd:sequence>
</xsd:complexType>
"""
from ...node import Node

class DocParamListItem(Node):
  def __init__(self, node):
    super.__init__(node)
  
  def get_parameternamelists(self):
    return self.get_children('parameternamelist', 'DocParamNameList')

  def get_parameterdescription(self):
    return self.get_child('parameterdescription', 'Description')