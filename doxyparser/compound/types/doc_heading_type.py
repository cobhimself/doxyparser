# This class has been auto-generated. To add/modify
# functionality, extend it.
from ..groups.doc_title_cmd_group import DocTitleCmdGroup

@attr('level')
class DocHeadingType(DocTitleCmdGroup):
    """Model representation of a doxygen docHeadingType type.

    Type XSD:

    <xsd:complexType xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="docHeadingType" mixed="true">
        <xsd:group ref="docTitleCmdGroup" minOccurs="0" maxOccurs="unbounded" />
        <xsd:attribute name="level" type="xsd:integer" /> 
      </xsd:complexType>
    """
