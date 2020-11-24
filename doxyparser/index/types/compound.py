from ...node import Node
from ...decorators import tag, collection


@tag('compound')
@collection(
    tag_name='member',
    xpath='/[@kind="{kind}"]',
    collectors={
        'functions': {'kind': 'function'},
        'variables': {'kind': 'variable'}
    })
class Compound(Node):
    """
    Model representation of a CompoundType Element from doxygen

    <xsd:complexType name="CompoundType">
    <xsd:sequence>
        <xsd:element name="name" type="xsd:string"/>
        <xsd:element name="member" type="MemberType" minOccurs="0" maxOccurs="unbounded"/>
    </xsd:sequence>
    <xsd:attribute name="refid" type="xsd:string" use="required"/>
    <xsd:attribute name="kind" type="CompoundKind" use="required"/>
    </xsd:complexType>

    """

    def get_name(self):
        return self.get_text('name')

    def get_refid(self):
        return self.get('refid')

    def get_kind(self):
        return self.get('kind')
