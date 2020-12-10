# This class has been auto-generated. To add/modify
# functionality, extend it.
from ...node import Node

@attr('lang')
@attr('version')
@collection('compounddef', '/[@kind={}]', {
    'classes': 'class',
    'structs': 'struct',
    'unions': 'union',
    'interfaces': 'interface',
    'protocols': 'protocol',
    'categories': 'category',
    'exceptions': 'exception',
    'services': 'service',
    'singletons': 'singleton',
    'modules': 'module',
    'types': 'type',
    'files': 'file',
    'namespaces': 'namespace',
    'groups': 'group',
    'pages': 'page',
    'examples': 'example',
    'dirs': 'dir',
})
@collection('compounddef', '/[@language={}]', {
    'Unknowns': 'Unknown',
    'IDLS': 'IDL',
    'Javas': 'Java',
    'C#S': 'C#',
    'DS': 'D',
    'PHPS': 'PHP',
    'Objective_Cs': 'Objective-C',
    'C++S': 'C++',
    'JavaScripts': 'JavaScript',
    'Pythons': 'Python',
    'Fortrans': 'Fortran',
    'VHDLS': 'VHDL',
    'XMLS': 'XML',
    'SQLS': 'SQL',
    'Markdowns': 'Markdown',
})
@collection('compounddef', '/[@prot={}]', {
    'publics': 'public',
    'protecteds': 'protected',
    'privates': 'private',
    'packages': 'package',
})
class DoxygenType(Node):
    """Model representation of a doxygen DoxygenType type.

    Type XSD:

    <xsd:complexType xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="DoxygenType">
        <xsd:sequence maxOccurs="unbounded">
          <xsd:element name="compounddef" type="compounddefType" minOccurs="0" />
        </xsd:sequence>
        <xsd:attribute name="version" type="DoxVersionNumber" use="required" />
        <xsd:attribute ref="xml:lang" use="required" />
      </xsd:complexType>
    """
