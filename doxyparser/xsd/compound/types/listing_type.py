# This class has been auto-generated. To add/modify
# functionality, extend it.
from ...node import Node

@attr('filename')
@collection('codeline', '/[@refkind={}]', {
    'compounds': 'compound',
    'members': 'member',
})
class ListingType(Node):
    """Model representation of a doxygen listingType type.

    Type XSD:

    <xsd:complexType xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="listingType">
        <xsd:sequence>
          <xsd:element name="codeline" type="codelineType" minOccurs="0" maxOccurs="unbounded" />
        </xsd:sequence>
        <xsd:attribute name="filename" type="xsd:string" use="optional" />
      </xsd:complexType>
    """
