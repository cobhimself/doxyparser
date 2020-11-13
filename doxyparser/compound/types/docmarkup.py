from ..groups.doccmdgroup import DocCmdGroup


class DocMarkup(DocCmdGroup):
    """
    Model representation of a docMarkupType from doxygen

    <xsd:complexType name="docMarkupType" mixed="true">
        <xsd:group ref="docCmdGroup" minOccurs="0" maxOccurs="unbounded" />
    </xsd:complexType>
    """
