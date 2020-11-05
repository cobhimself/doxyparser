#!/usr/bin/env python3
"""
Model representation of a docTitleType from doxygen

<xsd:complexType name="docTitleType" mixed="true">
  <xsd:group ref="docTitleCmdGroup" minOccurs="0" maxOccurs="unbounded" />
</xsd:complexType>
"""
from ..groups.doctitlecmdgroup import DocTitleCmdGroup

class DocTitle(DocTitleCmdGroup):
  pass