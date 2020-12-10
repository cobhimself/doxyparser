# This class has been auto-generated. To add/modify
# functionality, extend it.
from ...node import Node

@collection('member', '/[@prot={}]', {
    'publics': 'public',
    'protecteds': 'protected',
    'privates': 'private',
    'packages': 'package',
})
@collection('member', '/[@virt={}]', {
    'non_virtuals': 'non-virtual',
    'virtuals': 'virtual',
    'pure_virtuals': 'pure-virtual',
})
class ListofallmembersType(Node):
    """Model representation of a doxygen listofallmembersType type.

    Type XSD:

    <xsd:complexType xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="listofallmembersType">
        <xsd:sequence>
          <xsd:element name="member" type="memberRefType" minOccurs="0" maxOccurs="unbounded" />
        </xsd:sequence>
      </xsd:complexType>
    """
