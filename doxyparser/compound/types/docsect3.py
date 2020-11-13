"""
Model representation of a docSect3Type from doxygen

<xsd:complexType name="docSect3Type" mixed="true">
  <xsd:sequence>
    <xsd:element name="title" type="xsd:string" />
    <xsd:choice maxOccurs="unbounded">
      <xsd:element name="para" type="docParaType" minOccurs="0" maxOccurs="unbounded" />
      <xsd:element name="sect4" type="docSect4Type" minOccurs="0" maxOccurs="unbounded" />
      <xsd:element name="internal" type="docInternalS3Type" minOccurs="0" />
    </xsd:choice>
  </xsd:sequence>
  <xsd:attribute name="id" type="xsd:string" />
</xsd:complexType>
"""
from ...docsect import DocSect


class DocSect3(DocSect):
    def __init__(self, node, parser):
        super().__init__(node, parser, '3')

    def get_sect4s(self):
        return self.get_children('sect4', 'DocSect4')
