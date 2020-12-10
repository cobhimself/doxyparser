# This class has been auto-generated. To add/modify
# functionality, extend it.
from ...node import Node

@attr('lang')
@attr('version')
@collection('compound', '/[@kind={}]', {
    'classes': 'class',
    'structs': 'struct',
    'unions': 'union',
    'interfaces': 'interface',
    'protocols': 'protocol',
    'categories': 'category',
    'exceptions': 'exception',
    'files': 'file',
    'namespaces': 'namespace',
    'groups': 'group',
    'pages': 'page',
    'examples': 'example',
    'dirs': 'dir',
    'types': 'type',
})
class DoxygenType(Node):
    """Model representation of a doxygen DoxygenType type.

    Type XSD:

    <xsd:complexType xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="DoxygenType">
        <xsd:sequence>
          <xsd:element name="compound" type="CompoundType" minOccurs="0" maxOccurs="unbounded" />
        </xsd:sequence>
        <xsd:attribute name="version" type="xsd:string" use="required" />
        <xsd:attribute ref="xml:lang" use="required" />
      </xsd:complexType>
    """
