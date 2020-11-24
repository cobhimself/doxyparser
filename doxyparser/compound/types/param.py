from ...node import Node
from ...decorators import tag


@tag('param')
class Param(Node):
    """
    Model representation of a param Element from doxygen

    <xsd:complexType name="paramType">
    <xsd:sequence>
        <xsd:element name="attributes" minOccurs="0" />
        <xsd:element name="type" type="linkedTextType" minOccurs="0" />
        <xsd:element name="declname" minOccurs="0" />
        <xsd:element name="defname" minOccurs="0" />
        <xsd:element name="array" minOccurs="0" />
        <xsd:element name="defval" type="linkedTextType" minOccurs="0" />
        <xsd:element name="typeconstraint" type="linkedTextType" minOccurs="0" />
        <xsd:element name="briefdescription" type="descriptionType" minOccurs="0" />
    </xsd:sequence>
    </xsd:complexType>
    """

    def get_attributes(self):
        return self.get_text('attributes', '')

    def get_type(self):
        return self.get_child('type', 'LinkedText')

    def get_decl_name(self):
        return self.get_text('declname', '')

    def get_def_name(self):
        return self.get_text('defname', '')

    def get_array(self):
        return self.get_text('array', '')

    def get_def_val(self):
        return self.get_child('defval', 'LinkedText')

    def get_type_constraint(self):
        return self.get_child('typeconstraint', 'LinkedText')

    def get_brief_description(self):
        return self.get_child('briefdescription', 'Description')
