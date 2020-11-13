from ..groups.docvariablelistgroup import DocVariableListGroup


class DocVariableList(DocVariableListGroup):
    """
    Model representation of a docVariableListType from doxygen

    <xsd:complexType name="docVariableListType">
        <xsd:sequence>
            <xsd:group ref="docVariableListGroup" maxOccurs="unbounded" />
        </xsd:sequence>
    </xsd:complexType>
    """
