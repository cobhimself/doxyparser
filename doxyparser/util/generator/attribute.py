from xmlschema.validators import XsdAtomicBuiltin, XsdAtomicRestriction, XsdUnion
from .super import Super

class Attribute(Super):
    def get_name(self):
        return self._definition.local_name

    def get_type(self):
        my_type = self._definition.type
        name = ''
        if isinstance(my_type, XsdUnion):
            for i in my_type.member_types:
                if isinstance(i, XsdAtomicRestriction):
                    name = i.primitive_type.local_name
                    break
        elif isinstance(my_type, XsdAtomicBuiltin):
            name = my_type.local_name
        elif isinstance(my_type, XsdAtomicRestriction):
            name = my_type.primitive_type.local_name

        if name == 'string':
            name = 'str'

        return name

    def is_required(self):
        return self._definition.is_required

    def is_optional(self):
        return self._definition.is_optional

    def get_decorator(self):
        return "@attr('{}', {})".format(self.get_name(), self.get_type())
