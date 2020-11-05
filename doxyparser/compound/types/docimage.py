#!/usr/bin/env python3
"""
Model representation of a docimage type from doxygen

<xsd:complexType name="docImageType" mixed="true">
  <xsd:group ref="docTitleCmdGroup" minOccurs="0" maxOccurs="unbounded" />
  <xsd:attribute name="type" type="DoxImageKind" use="optional"/>
  <xsd:attribute name="name" type="xsd:string" use="optional"/>
  <xsd:attribute name="width" type="xsd:string" use="optional"/>
  <xsd:attribute name="height" type="xsd:string" use="optional"/>
  <xsd:attribute name="inline" type="DoxBool" use="optional"/>
  <xsd:attribute name="caption" type="xsd:string" use="optional"/>
</xsd:complexType>
"""
from ..groups.doctitlecmdgroup import DocTitleCmdGroup

class DocImage(DocTitleCmdGroup):
  def __init__(self, node):
      super.__init__(node)
  
  def get_type(self):
    return self.get('type')
  
  def get_name(self):
    return self.get('name')
  
  def get_width(self):
    return self.get('width')
  
  def get_height(self):
    return self.get('height')
  
  def is_inline(self):
    return self.get_bool('inline')
  
  def get_caption(self):
    return self.get('caption')