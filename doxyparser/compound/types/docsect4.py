"""
Model representation of a docSect4Type from doxygen

<xsd:complexType name="docSect4Type" mixed="true">
  <xsd:sequence>
    <xsd:element name="title" type="xsd:string" />
    <xsd:choice maxOccurs="unbounded">
      <xsd:element name="para" type="docParaType" minOccurs="0" maxOccurs="unbounded" />
      <xsd:element name="internal" type="docInternalS4Type" minOccurs="0" />
    </xsd:choice>
  </xsd:sequence>
  <xsd:attribute name="id" type="xsd:string" />
</xsd:complexType>
"""
from ...docsect import DocSect


class DocSect4(DocSect):
    def __init__(self, node, parser):
        super.__init__(node, parser, '4')
