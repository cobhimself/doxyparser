from ...node import Node


class DocFormulaType(Node):
    """
    Model representation of a docFormulaType from doxygen

    <xsd:complexType name="docFormulaType" mixed="true">
        <xsd:attribute name="id" type="xsd:string" />
    </xsd:complexType>
    """

    def get_id(self):
        return self.get('id')
