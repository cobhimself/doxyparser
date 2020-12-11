from xmlschema.validators.attributes import XsdAnyAttribute

from .typeable import Typeable

class Attribute(Typeable):
    """Class responsible for holding information relating to xsd schema
    attributes
    """

    def __init__(self, element, parent):
        self._enums = None
        self._parent = parent
        super().__init__(element)

    def get_name(self):
        return self._definition.local_name

    def is_any_attribute(self):
        return isinstance(self.get_definition(), XsdAnyAttribute)

    def is_enum(self):
        return len(self.get_enum_values()) > 0

    def get_enum_values(self):

        if self._enums is None:
            resolved = None
            my_type = self.get_definition().type
            if my_type.is_union():
                for i in my_type.member_types:
                    if i.is_restriction():
                        resolved = i
                        break
            elif my_type.is_restriction():
                resolved = my_type

            if resolved is None:
                self._enums = []
            else:
                if resolved.is_simple():
                    self._enums = [] if resolved.enumeration is None or resolved.enumeration == [''] else resolved.enumeration

        return self._enums


    def is_required(self):
        return self._definition.is_required

    def is_optional(self):
        return self._definition.is_optional

    def get_decorator(self):
        return "@attr('{}', {})".format(self.get_name(), self.get_type())
