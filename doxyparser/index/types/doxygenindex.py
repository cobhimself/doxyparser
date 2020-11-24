from ...node import Node
from ...decorators import collection, tag


@tag('doxygenindex')
@collection(
    tag_name='compound',
    xpath='/[@kind="{kind}"]',
    collectors={
        'classes': {'kind': 'class'},
        'interfaces': {'kind': 'interface'},
        'namespaces': {'kind': 'namespace'},
        'files': {'kind': 'file'},
        'dirs': {'kind': 'dir'}
    })
class DoxygenIndex(Node):
    """
    Model representation of a doxygenindex Element from doxygen

    <xsd:complexType name="DoxygenType">
    <xsd:sequence>
        <xsd:element name="compound" type="CompoundType" minOccurs="0" maxOccurs="unbounded"/>
    </xsd:sequence>
    <xsd:attribute name="version" type="xsd:string" use="required"/>
    <xsd:attribute ref="xml:lang" use="required"/>
    </xsd:complexType>
    """

    def get_version(self):
        return self.get('version')
