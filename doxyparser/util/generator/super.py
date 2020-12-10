from doxyparser.util.element_generator import cache

class Super():

    def __init__(self, definition):
        self._definition = definition
        self._built = False

    def get_definition(self):
        return self._definition

    def get_type_from_cache(self, type_name):
        return cache.get_type(type_name)

    def get_group_from_cache(self, group_name):
        return cache.get_group(group_name)

    def get_cache(self):
        return cache

    def build_content(self):
        if not self._built:
            from doxyparser.util.generator.element import Element
            from doxyparser.util.generator.attribute import Attribute
            definition = self.get_definition()
            if definition.has_complex_content():
                for component in definition.get_content().iter_components():
                    if isinstance(component, XsdGroup):
                        self._build_group(component)
                    elif isinstance(component, XsdElement):
                        self._build_element(component)
                    else:
                        breakpoint()
                        print(component)

            for attr_name, attr in self.get_definition().attributes.items():
                self._attr[attr_name] = Attribute(attr, self)


        self._built = True

    def _build_group(self, group):
        if group.ref is not None:
            group_ref = self.get_group_from_cache(group.name)
            self._group[group.name] = group_ref
        else:
            for component in group.iter_components():
                is_group = isinstance(component, XsdGroup)
                if component == group or (is_group and component.ref is None):
                    continue
                if is_group:
                    self._build_group(component)
                elif isinstance(component, XsdElement):
                    self._build_element(component)
                else:
                    breakpoint()
                    print(component)

    def _build_element(self, element):
        from .element import Element
        node_type = self.get_type_from_cache(element.type)
        self._elem[element.name] = Element(element, node_type)