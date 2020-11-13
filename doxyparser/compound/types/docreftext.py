#!/usr/bin/env python3
"""
Model representation of a docRefTextType from doxygen

<xsd:complexType name="docRefTextType" mixed="true">
  <xsd:group ref="docTitleCmdGroup" minOccurs="0" maxOccurs="unbounded" />
  <xsd:attribute name="refid" type="xsd:string" />
  <xsd:attribute name="kindref" type="DoxRefKind" />
  <xsd:attribute name="external" type="xsd:string" />
</xsd:complexType>
"""
from ..groups.doctitlecmdgroup import DocTitleCmdGroup

class DocParBlock(DocTitleCmdGroup):
  def get_refid(self):
    return self.get('refid')
  
  def get_kindref(self):
    return self.get('kindref')
  
  def get_external(self):
    return self.get('external')