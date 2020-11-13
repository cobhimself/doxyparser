from ...node import Node


class DocHtmlOnly(Node):
    """
    Model representation of a dochtmlonly type from doxygen

    <xsd:complexType name="docHtmlOnlyType">
        <xsd:simpleContent>
            <xsd:extension base="xsd:string">
                <xsd:attribute name="block" type="xsd:string" />
            </xsd:extension>
        </xsd:simpleContent>
    </xsd:complexType>
    """

    def get_block(self):
        return self.get('block')
