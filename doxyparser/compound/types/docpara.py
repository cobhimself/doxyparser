from ..groups.doccmdgroup import DocCmdGroup


class DocPara(DocCmdGroup):
    """
    Model representation of a docpara type from doxygen

    <xsd:complexType name="docParaType" mixed="true">
        <xsd:group ref="docCmdGroup" minOccurs="0" maxOccurs="unbounded" />
    </xsd:complexType>
    """
