# This class has been auto-generated. To add/modify
# functionality, extend it.
from ...node import Node

@attr('id')
@collection('childnode', '/[@relation={}]', {
    'includes': 'include',
    'usages': 'usage',
    'template_instances': 'template-instance',
    'public_inheritances': 'public-inheritance',
    'protected_inheritances': 'protected-inheritance',
    'private_inheritances': 'private-inheritance',
    'type_constraints': 'type-constraint',
})
@element('label', 'any')
@element('link', 'linkType')
class NodeType(Node):
    """Model representation of a doxygen nodeType type.

    Type XSD:

    <xsd:complexType xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="nodeType">
        <xsd:sequence>
          <xsd:element name="label" />
          <xsd:element name="link" type="linkType" minOccurs="0" />
          <xsd:element name="childnode" type="childnodeType" minOccurs="0" maxOccurs="unbounded" />
        </xsd:sequence>
        <xsd:attribute name="id" type="xsd:string" />
      </xsd:complexType>
    """
