# This class has been auto-generated. To add/modify
# functionality, extend it.
from ..groups.doc_title_cmd_group import DocTitleCmdGroup

@attr('caption')
@attr('height')
@attr('name')
@attr('width')
@boolattr('inline')
class DocImageType(DocTitleCmdGroup):
    """Model representation of a doxygen docImageType type.

    Type XSD:

    <xsd:complexType xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="docImageType" mixed="true">
        <xsd:group ref="docTitleCmdGroup" minOccurs="0" maxOccurs="unbounded" />
        <xsd:attribute name="type" type="DoxImageKind" use="optional" />
        <xsd:attribute name="name" type="xsd:string" use="optional" />
        <xsd:attribute name="width" type="xsd:string" use="optional" />
        <xsd:attribute name="height" type="xsd:string" use="optional" />
        <xsd:attribute name="inline" type="DoxBool" use="optional" />
        <xsd:attribute name="caption" type="xsd:string" use="optional" />
      </xsd:complexType>
    """
