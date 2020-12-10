# This class has been auto-generated. To add/modify
# functionality, extend it.
from ..groups.doc_title_cmd_group import DocTitleCmdGroup

@attr('id')
class DocTocItemType(DocTitleCmdGroup):
    """Model representation of a doxygen docTocItemType type.

    Type XSD:

    <xsd:complexType xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="docTocItemType" mixed="true">
        <xsd:group ref="docTitleCmdGroup" minOccurs="0" maxOccurs="unbounded" />
        <xsd:attribute name="id" type="xsd:string" /> 
      </xsd:complexType>
    """
