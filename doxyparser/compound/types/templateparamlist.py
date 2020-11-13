from ...node import Node


class TemplateParamList(Node):
    """
    Model representation of a templateparamlist Element from doxygen

    <xsd:complexType name="templateparamlistType">
        <xsd:sequence>
            <xsd:element name="param" type="paramType" minOccurs="0" maxOccurs="unbounded" />
        </xsd:sequence>
    </xsd:complexType>
    """

    def get_params(self):
        return self.get_children('param', 'Param')
