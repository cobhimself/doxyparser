# This class has been auto-generated. To add/modify
# functionality, extend it.
from ...node import Node

@collection('ref', '/[@kindref={}]', {
    'compounds': 'compound',
    'members': 'member',
})
@element('sp', 'spType')
class HighlightType(Node):
    """Model representation of a doxygen highlightType type.

    Type XSD:

    <xsd:complexType xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="highlightType" mixed="true">
        <xsd:choice minOccurs="0" maxOccurs="unbounded">
          <xsd:element name="sp" type="spType" />
          <xsd:element name="ref" type="refTextType" />
        </xsd:choice>
        <xsd:attribute name="class" type="DoxHighlightClass" />
      </xsd:complexType>
    """
