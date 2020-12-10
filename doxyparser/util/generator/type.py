from .buildable import Buildable

class Type(Buildable):
    def get_name(self):
        """Get the name of this type.

        Returns:
            str: The name of this type.
        """
        return self.get_definition().name

    def has_content(self):
        """Determine whether or not this type has either nested elements
        or text.

        Returns:
            bool: True if there is content in this type, False otherwise.
        """
        return self.get_definition().content is not None

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
        return self.get_definition().content

    def has_simple_content(self):
        """Determine whether or not this type denys element content but
        allows text content.

        Returns:
            bool: True if only text content is allowed, False otherwise.
        """
        return self.has_content() and self.get_definition().has_simple_content()

    def has_complex_content(self):
        return self.has_content() and self.get_definition().has_complex_content()

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
        return self.get_definition().has_simple_content()

    def allows_elements_and_text(self):
        """Alias method for has_mixed_content()

        Returns:
            bool: True if this type allows elements and/or text. False
                otherwise.
        """
        return self.has_mixed_content()

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