from ..types.compoundref import CompoundRefType
from ...decorators import tag


@tag('basecompoundref')
class BaseCompoundRef(CompoundRefType):
    """
    Model representation of a basecompoundref Element from doxygen

    <xsd:element name="basecompoundref" type="compoundRefType" minOccurs="0" maxOccurs="unbounded" />
    """