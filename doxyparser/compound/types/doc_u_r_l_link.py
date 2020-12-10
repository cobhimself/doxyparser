# This class has been auto-generated. To add/modify
# functionality, extend it.
from ..groups.doc_title_cmd_group import DocTitleCmdGroup

@attr('url')
class DocURLLink(DocTitleCmdGroup):
    """Model representation of a doxygen docURLLink type.

    Type XSD:

    <xsd:complexType xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="docURLLink" mixed="true">
        <xsd:group ref="docTitleCmdGroup" minOccurs="0" maxOccurs="unbounded" />
        <xsd:attribute name="url" type="xsd:string" />
      </xsd:complexType>
    """
