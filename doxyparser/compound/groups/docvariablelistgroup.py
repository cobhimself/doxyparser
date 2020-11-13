from ...nodegroup import NodeGroup


class DocVariableListGroup(NodeGroup):
    """
    Model representation of a docVariableListGroup type from doxygen

    <xsd:group name="docVariableListGroup">
        <xsd:sequence>
            <xsd:element name="varlistentry" type="docVarListEntryType" />
            <xsd:element name="listitem" type="docListItemType" />
        </xsd:sequence>
    </xsd:group>
    """

    def get_varlistentry(self):
        return self.get_child('varlistentry', 'DocVarListEntry')

    def get_listitem(self):
        return self.get_child('listitem', 'DocListItem')
