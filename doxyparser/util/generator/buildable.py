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
from xmlschema.validators import XsdGroup
from xmlschema.validators.elements import XsdElement
from xmlschema.validators.attributes import XsdAttributeGroup, XsdAttribute, XsdAnyAttribute
from .super import Super


class Buildable(Super):
    """Provides a class with the ability to build doxyparser-specific data
    relating to XSD attributes, elements and groups.
    """
    def __init__(self, definition):
        super().__init__(definition)
        self._attr = {}
        self._elem = {}
        self._group = {}
        self._built = False

    def _build(self):
        """Build the internal types of the components in this class'
        definition.
        """
        if not self._built:
            from doxyparser.util.generator.attribute import Attribute
            definition = self.get_definition()
            for component in definition.iter_components():
                if component == definition:
                    continue
                if isinstance(component, XsdAttributeGroup):
                    continue
                if isinstance(component, XsdAttribute):
                    continue
                if isinstance(component, XsdAnyAttribute):
                    continue
                if isinstance(component, XsdGroup):
                    self._build_group(component)
                elif isinstance(component, XsdElement):
                    self._build_element(component)
                else:
                    breakpoint()
                    print(component)

            if hasattr(definition, 'attributes'):
                for attr_name, attr in definition.attributes.items():
                    self._attr[attr_name] = Attribute(attr, self)

        self._built = True

    def _build_group(self, group):
        """Iterate through the group's components and add them to this
        buildable object.

        Args:
            group (XsdGroup): The group to build
        Raises:
            Exception: if we're not currently handline all of the components,
                make it known.
        """
        # This group references a complex type
        if group.ref is not None:
            group_ref = self.get_group_from_cache(group.name)
            self._group[group.name] = group_ref
        else:
            for component in group.iter_components():
                is_group = isinstance(component, XsdGroup)
                # Iterating the components usually returns the group itself so
                # we check to make sure our component isn't the group itself.
                # Also, for groups within groups, we don't want to traverse
                # deeply because it would mean we going into the elements of
                # the child group. We just want a reference to the group's
                # name.
                if component == group or (is_group and component.ref is None):
                    continue
                if is_group:
                    # self._build_group(component)
                    # Since we don't want to dive deeper into child groups,
                    # continue.
                    continue

                if isinstance(component, XsdElement):
                    self._build_element(component)
                else:
                    # Seems we've encountered a component we haven't prepared
                    # for. Make it known.
                    raise Exception(
                        f'Unhandled component {component} during build process!')

    def _build_element(self, element):
        from .element import Element
        node_type = self.get_type_from_cache(element.type)
        self._elem[element.name] = Element(element, node_type)

    def get_attributes(self):
        """Get a list of Attributes associated with this type.

        Returns:
            Attribute[]: A list of Attribute models for the attributes in
                this type.
        """
        self._build()
        return self._attr

    def get_elements(self):
        """Return a list of Elements associated with this type.

        Returns:
            Element[]: A list of Element models for the elements in this
                type.
        """
        self._build()
        return self._elem

    def get_groups(self):
        """Get the groups associated with this object.

        Returns:
            dict: Returns a dict with group names as keys and Group objects
                as values.
        """
        self._build()
        return self._group
