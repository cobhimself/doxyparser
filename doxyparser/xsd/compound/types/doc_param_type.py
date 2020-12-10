# This class has been auto-generated. To add/modify
# functionality, extend it.
from ...node import Node

@collection('ref', '/[@kindref={}]', {
    'compounds': 'compound',
    'members': 'member',
})
class DocParamType(Node):
    """Model representation of a doxygen docParamType type.

    Type XSD:

    <xsd:complexType xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="docParamType" mixed="true">
        <xsd:sequence>
          <xsd:element name="ref" type="refTextType" minOccurs="0" maxOccurs="1" />
        </xsd:sequence>
      </xsd:complexType>
    """
