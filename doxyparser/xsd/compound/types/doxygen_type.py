"""
MIT License

Copyright (c) 2020 Collin Brooks

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

This class has been auto-generated. To add/modify functionality, extend it.
See util/generator/element_generator.py
"""
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
