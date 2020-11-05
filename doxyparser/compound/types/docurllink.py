#!/usr/bin/env python3
"""
Model representation of a docURLLink from doxygen

<xsd:complexType name="docURLLink" mixed="true">
  <xsd:group ref="docTitleCmdGroup" minOccurs="0" maxOccurs="unbounded" />
  <xsd:attribute name="url" type="xsd:string" />
</xsd:complexType>
"""
from ..groups.doctitlecmdgroup import DocTitleCmdGroup

class DocURLLink(DocTitleCmdGroup):
  def __init__(self, node):
    super.__init__(node)
  
  def get_url(self):
    return self.get('url')
  