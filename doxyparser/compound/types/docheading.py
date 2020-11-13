"""
Model representation of a docheading type Element from doxygen

<xsd:complexType name="docHeadingType" mixed="true">
  <xsd:group ref="docTitleCmdGroup" minOccurs="0" maxOccurs="unbounded" />
  <xsd:attribute name="level" type="xsd:integer" /> <!-- todo: range 1-6 -->
</xsd:complexType>
"""
from ..groups.doctitlecmdgroup import DocTitleCmdGroup


class DocCopy(DocTitleCmdGroup):

    def get_level(self):
        return self.get('level')
