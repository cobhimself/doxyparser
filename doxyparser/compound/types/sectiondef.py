from ...node import Node
from ...decorators import tag


@tag('sectiondef')
class SectionDef(Node):
    """
    Model representation of a sectiondef Element from doxygen

    <xsd:complexType name="sectiondefType">
    <xsd:sequence>
        <xsd:element name="header" type="xsd:string" minOccurs="0" />
        <xsd:element name="description" type="descriptionType" minOccurs="0" />
        <xsd:element name="memberdef" type="memberdefType" maxOccurs="unbounded" />
    </xsd:sequence>
    <xsd:attribute name="kind" type="DoxSectionKind" />
    </xsd:complexType>
    """

    def get_member_defs(self):
        return self.get_children('memberdef', 'MemberDef')

    def get_header(self):
        return self.get_text('header', '')

    def get_description(self):
        return self.get_child('description', 'Description')

    def get_kind(self):
        return self.get('kind')
