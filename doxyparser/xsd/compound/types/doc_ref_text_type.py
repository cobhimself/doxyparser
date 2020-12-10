# This class has been auto-generated. To add/modify
# functionality, extend it.
from ..groups.doc_title_cmd_group import DocTitleCmdGroup

@attr('external')
@attr('refid')
class DocRefTextType(DocTitleCmdGroup):
    """Model representation of a doxygen docRefTextType type.

    Type XSD:

    <xsd:complexType xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="docRefTextType" mixed="true">
        <xsd:group ref="docTitleCmdGroup" minOccurs="0" maxOccurs="unbounded" />
        <xsd:attribute name="refid" type="xsd:string" />
        <xsd:attribute name="kindref" type="DoxRefKind" />
        <xsd:attribute name="external" type="xsd:string" />
      </xsd:complexType>
    """
