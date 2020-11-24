from ..types.docformula import DocFormulaType
from ...decorators import tag


@tag('formula')
class Formula(DocFormulaType):
    """
    Model representation of a formula Element from doxygen

    <xsd:element name="formula" type="docFormulaType" />
    """
