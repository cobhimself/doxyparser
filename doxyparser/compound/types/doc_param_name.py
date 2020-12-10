# This class has been auto-generated. To add/modify
# functionality, extend it.
from ...node import Node

@collection('ref', '/[@kindref={}]', {
    'compounds': 'compound',
    'members': 'member',
})
class DocParamName(Node):
    """Model representation of a doxygen docParamName type.

    Type XSD:

    <xsd:complexType xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="docParamName" mixed="true">
        <xsd:sequence>
          <xsd:element name="ref" type="refTextType" minOccurs="0" maxOccurs="1" />
        </xsd:sequence>
        <xsd:attribute name="direction" type="DoxParamDir" use="optional" />
      </xsd:complexType>
    """
