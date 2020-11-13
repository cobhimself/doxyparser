from ...node import Node


class DocEmoji(Node):
    """
    Model representation of a docemoji type from doxygen

    <xsd:complexType name="docEmojiType">
        <xsd:attribute name="name" type="xsd:string"/>
        <xsd:attribute name="unicode" type="xsd:string"/>
    </xsd:complexType>
    """
    def get_name(self):
        return self.get('name')

    def get_unicode(self):
        return self.get('unicode')
