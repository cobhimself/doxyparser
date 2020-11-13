from ...node import Node


class DocAnchor(Node):
    """
    Model representation of a docanchor type from doxygen

    <xsd:complexType name="docAnchorType" mixed="true">
        <xsd:attribute name="id" type="xsd:string" />
    </xsd:complexType>
    """

    def get_id(self):
        return self.get('id')
