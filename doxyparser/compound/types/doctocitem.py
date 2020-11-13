from ..groups.doctitlecmdgroup import DocTitleCmdGroup


class DocTocItem(DocTitleCmdGroup):
    """
    Model representation of a docTocItemType from doxygen

    <xsd:complexType name="docTocItemType" mixed="true">
        <xsd:group ref="docTitleCmdGroup" minOccurs="0" maxOccurs="unbounded" />
        <xsd:attribute name="id" type="xsd:string" />
    </xsd:complexType>
    """

    def get_id(self):
        return self.get('id')
