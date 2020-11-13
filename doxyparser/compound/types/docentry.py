#!/usr/bin/env python3
"""
Model representation of a docEntryType from doxygen

<xsd:complexType name="docEntryType">
  <xsd:sequence>
    <xsd:element name="para" type="docParaType" minOccurs="0" maxOccurs="unbounded" />
  </xsd:sequence>
  <xsd:attribute name="thead" type="DoxBool" />
  <xsd:attribute name="colspan" type="xsd:integer" />
  <xsd:attribute name="rowspan" type="xsd:integer" />
  <xsd:attribute name="align" type="DoxAlign" />
  <xsd:attribute name="class" type="xsd:string" />
  <xsd:anyAttribute processContents="skip"/>
</xsd:complexType>
"""
from ...node import Node

class DocEntry(Node):
  def get_paras(self):
    return self.get_children('para', 'DocPara')  
  
  def has_thead(self):
    return self.get_bool('thead')
  
  def get_colspan(self):
    return self.get('colspan')
  
  def get_rowspan(self):
    return self.get('rowspan')
  
  def get_align(self):
    return self.get('align')
  
  def get_class(self):
    return self.get('class')