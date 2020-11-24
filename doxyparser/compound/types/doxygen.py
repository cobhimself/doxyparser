from ...node import Node
from typing import Optional
from ...compound.types.compounddef import CompoundDef
from ...decorators import collection


class Doxygen(Node):
    """
    Model representation of a doxygen element from doxygen's compound.xsd

    <xsd:element name="doxygen" type="DoxygenType"/>

    <xsd:complexType name="DoxygenType">
        <xsd:sequence maxOccurs="unbounded">
            <xsd:element name="compounddef" type="compounddefType" minOccurs="0" />
        </xsd:sequence>
        <xsd:attribute name="version" type="DoxVersionNumber" use="required" />
        <xsd:attribute ref="xml:lang" use="required"/>
    </xsd:complexType>
    """

    @collection('compounddef', '/[@kind="{}"]')
    def get_compounddefs(
        self,
        kind: Optional[str] = None
    ) -> dict[CompoundDef]:
        path = '' if kind is None else '/[@kind="' + kind + '"]'
        return self.get_children(
            tag='compounddef',
            path=path
        )

    def get_namespace_compounddefs(self):
        return self.get_compounddefs('namespace')

    def get_class_compounddefs(self):
        return self.get_compounddefs('class')

    def get_version(self):
        return self.get('version')
