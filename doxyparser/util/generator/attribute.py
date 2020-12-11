"""
MIT License

Copyright (c) 2020 Collin Brooks

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
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
        """Get the name of this attribute.

        Returns:
            string: The local name of this attribute
        """
        return self._definition.local_name

    def is_any_attribute(self):
        """Determine if this attribute is an XsdAnyAttribute.

        Returns:
            bool
        """
        return isinstance(self.get_definition(), XsdAnyAttribute)

    def is_enum(self):
        """Determine whether or not this attribute has enum values.

        Returns:
            bool
        """
        return len(self.get_enum_values()) > 0

    def get_enum_values(self):
        """Get the enum values associated with this attribute.

        For types that are union types, we dig deep into them to find whether
        or not any of their members have enum values.

        Returns:
            list: A list of enum values
        """

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
                    self._enums = [] if resolved.enumeration is None or resolved.enumeration == [
                        ''] else resolved.enumeration

        return self._enums

    def is_required(self):
        """Determine whether or not this attribute is required.

        Returns:
            bool
        """
        return self._definition.is_required

    def is_optional(self):
        """Determine whether or not this attribute is optional.

        Returns:
            bool
        """
        return self._definition.is_optional
