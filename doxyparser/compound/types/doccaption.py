#!/usr/bin/env python3
"""
Model representation of a docCaptionType from doxygen

<xsd:complexType name="docCaptionType" mixed="true">
  <xsd:group ref="docTitleCmdGroup" minOccurs="0" maxOccurs="unbounded" />
</xsd:complexType>
"""
from ..groups.doctitlecmdgroup import DocTitleCmdGroup

class DocCaption(DocTitleCmdGroup):
  pass