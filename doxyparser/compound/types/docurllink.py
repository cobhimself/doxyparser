"""
Model representation of a docURLLink from doxygen

<xsd:complexType name="docURLLink" mixed="true">
  <xsd:group ref="docTitleCmdGroup" minOccurs="0" maxOccurs="unbounded" />
  <xsd:attribute name="url" type="xsd:string" />
</xsd:complexType>
"""
from ..groups.doctitlecmdgroup import DocTitleCmdGroup


class DocURLLink(DocTitleCmdGroup):
    def get_url(self):
        return self.get('url')
