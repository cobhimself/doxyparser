from xml.etree.ElementTree import tostring
from xmlschema.validators import XsdAtomicBuiltin, XsdAtomicRestriction, XsdUnion, XsdGroup
from ..wrap import wrap, wrapxml
from .super import Super

class Type(Super):

    def __init__(self, element):
        super().__init__(element)
        self._attr = {}
        self._elem = {}

    def get_name(self):
        """Get the name of this type.

        Returns:
            str: The name of this type.
        """
        return self._definition.name

    def has_content(self):
        """Determine whether or not this type has either nested elements
        or text.

        Returns:
            bool: True if there is content in this type, False otherwise.
        """
        return self._definition.content is not None

    def has_empty_content(self):
        """Determine whether or not this type's content is empty.

        If the type does not support content, it is considered to have empty
        content.

        Returns:
            bool: True if there is content, False otherwise.
        """
        return not self.has_content() or self.get_content().is_empty()

    def is_placeholder(self):
        """Determine whether or not this type is a simple placeholder.

        A placeholder is defined as an element with no attributes and no content.

        Ex: <hr/>

        Returns:
            bool: True if this is a placeholder type, false otherwise
        """
        return (self.is_empty()
            and self.has_empty_content()
            and not self.has_attributes())

    def has_attributes(self):
        """Determine whether or not this type has attributes.

        Returns:
            bool: True if this type has attributes, False otherwise.
        """
        return len(self.get_definition().attributes) > 0

    def get_content(self):
        """Get the content of this type.

        Returns:
            mixed: None if no content exists, mixed otherwise.
        """
        return self._definition.content

    def has_simple_content(self):
        """Determine whether or not this type denys element content but
        allows text content.

        Returns:
            bool: True if only text content is allowed, False otherwise.
        """
        return self.has_content() and self.get_content().has_simple_content()

    def has_element_only_content(self):
        """Determine whether or not this type allows child elements but denys
        intermingled text content.

        Returns:
            bool: True if this element does not contain text intermingled
                with elements; False otherwise.
        """
        return self.has_content() and self.get_content().is_element_only()

    def has_mixed_content(self):
        """Determine whether or not this type allows child elements and
        intermingled text.

        Returns:
            bool: True if this type allows elements and intermingled text;
                False otherwise.
        """
        return self.has_content() and self.get_content().has_mixed_content()

    def is_simple(self):
        """Determine whether or not this type is a simple type.

        Simple types do not allow attributes or element content.

        Returns:
            bool: True if this type is a simple type; False otherwise.
        """
        return self.get_definition().is_simple()

    def is_complex(self):
        """Determine whether or not this type is a complex type.

        Complex types allow attributes and/or element content.

        Returns:
            bool: True if this type is a complex type, False otherwise.
        """
        return self.get_definition().is_complex()

    def is_empty(self):
        return self.get_definition().is_empty()

    def is_element_only(self):
        return self.get_definition().is_element_only()

    def is_any_type(self):
        return self.get_local_name() == 'anyType'


    def is_text_only(self):
        return self._definition.has_simple_content()

    def allows_elements_and_text(self):
        """Alias method for has_mixed_content()

        Returns:
            bool: True if this type allows elements and/or text. False
                otherwise.
        """
        return self.has_mixed_content()

    def get_attributes(self):
        """Get a list of Attributes associated with this type.

        Returns:
            Attribute[]: A list of Attribute models for the attributes in
                this type.
        """
        if len(self._attr) == 0:
            from .attribute import Attribute
            for attr_name, attr in self._definition.attributes.items():
                self._attr[attr_name] = Attribute(attr, self)

        return self._attr

    def get_elements(self):
        """Return a list of Elements associated with this type.

        Returns:
            Element[]: A list of Element models for the elements in this
                type.
        """
        if len(self._elem) == 0:
            from .element import Element
            if self._definition.has_complex_content():
                for elem in self._definition.content.iter_elements():
                    self._elem[elem.name] = Element(elem, Type(elem.type))

        return self._elem

    def get_local_name(self):
        my_type = self.get_definition()
        name = my_type.name
        local_name = my_type.local_name
        if local_name is not None and local_name == 'string':
            return 'str'
        elif name is None:
            if my_type.is_union():
                for i in my_type.member_types:
                    if i.is_restriction():
                        name = i.primitive_type.local_name
                        break
            elif my_type.is_restriction():
                name = my_type.primitive_type.local_name
            elif isinstance(my_type, XsdAtomicBuiltin):
                name = my_type.local_name
        else:
            name = my_type.local_name

        return name