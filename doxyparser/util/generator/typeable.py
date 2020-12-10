from xmlschema.validators.attributes import XsdAnyAttribute
from .super import Super
from .type import Type

class Typeable(Super):
    def __init__(self, definition, type_instance=None):
        if type_instance is None:
            self._type = Type(
                definition if isinstance(definition, XsdAnyAttribute)
                else definition.type
            )
        else:
            self._type = type_instance

        super().__init__(definition)

    def get_type(self):
        return self._type

    def get_type_local_name(self):
        return self.get_type().get_local_name()

    def is_any_type(self):
        return self.get_type().is_any_type()

    def is_dox_bool(self):
        return self.get_definition().type.name == 'DoxBool'

    def get_type_name(self):
        return self.get_type().get_name()

    def has_content(self):
        return self.get_type().has_content()

    def get_content(self):
        return self.get_type().get_content()

    def is_element_only(self):
        return self.get_type().is_element_only()

    def is_simple(self):
        return self.get_type().is_simple()

    def is_text_only(self):
        return self.get_type().is_text_only()

    def is_complex(self):
        return self.get_type().is_complex()

    def is_placeholder(self):
        return self.get_type().is_placeholder()
