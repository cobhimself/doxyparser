from ..types.compoundref import CompoundRefType
from ...decorators import tag


@tag('basecompoundref')
class DerivedCompoundRef(CompoundRefType):
    """
    Model representation of a derivedcompoundref Element from doxygen

    <xsd:element name="derivedcompoundref" type="compoundRefType" minOccurs="0" maxOccurs="unbounded" />
    """