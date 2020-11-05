#!/usr/bin/env python3
"""
Model representation of a docTocItemType from doxygen

<xsd:complexType name="docTocItemType" mixed="true">
  <xsd:group ref="docTitleCmdGroup" minOccurs="0" maxOccurs="unbounded" />
  <xsd:attribute name="id" type="xsd:string" /> 
</xsd:complexType>
"""
from ..groups.doctitlecmdgroup import DocTitleCmdGroup

class DocTocItem(DocTitleCmdGroup):
  def __init__(self, node):
    super.__init__(node)
  
  def get_id(self):
    return self.get('id')