from .ref import Ref


class InnerClass(Ref):
    """
    Model representation of a innerclass element from doxygen

    <xsd:element name="innerclass" type="refType" minOccurs="0" maxOccurs="unbounded" />
    """

    def get_class_name(self):
      return self._node.text