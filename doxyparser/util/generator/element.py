import pyinputplus
import textwrap
import inflect
from .attribute import Attribute
from .super import Super
from ..wrap import wrap

class Element(Super):
    def __init__(self, element, node_type):
        self._type = node_type
        self._attr = {}
        super().__init__(element)

    def get_name(self):
        return self._definition.name

    def get_content(self):
        return self._definition.type.content

    def is_element_only(self):
        return self.get_type().is_element_only()

    def is_multiple(self):
        return self._definition.is_multiple()

    def is_single(self):
        return self._definition.is_single()

    def is_text_only(self):
        return self.get_type().has_simple_content()

    def allows_elements_and_text(self):
        return self.get_type().has_mixed_content()

    def get_type(self):
        return self._definition.type

    def get_attributes(self):
        if len(self._attr) == 0:
            for attr_name, attr in self._definition.attributes.items():
                self._attr[attr_name] = Attribute(attr)

        return self._attr

    def get_attribute_by_name(self, name):
        return self._attr.get(name, None)

    def get_decorator(self):
        attributes = self.get_attributes().values()
        parent = self._definition.parent.parent.name
        type_name = self.get_type().name
        name = self.get_name()

        if self.is_single():
            return f"@element(name='{name}', type='simple')"

        do_filter = pyinputplus.inputYesNo(
            f"'{parent}' has a sequence of '{name}' elements with the type '{type_name}'. Would you like to be able to filter the collection? [Y|y|N|n]\n",
            default="Y"
        )

        if do_filter:
            filter_by = pyinputplus.inputMenu(
                [attr.get_name() for attr in attributes],
                prompt="Which attribute should we allow filtering with?\n"
            )

            decorator = textwrap.dedent(f"""
            @collection(tag_name='{name}',
                xpath='/[@{filter_by}={{{filter_by}}}]',
                """).strip()

            attr = self.get_attribute_by_name(filter_by)
            collectors = []
            for enum in attr.get_definition().type.enumeration:
                collectors.append(f"'{inflect.engine().plural(enum)}': {{'{filter_by}': '{enum}'}}")

            decorator += "\n    collectors={\n"
            decorator += wrap(",\n".join(collectors), '        ', '        ')
            decorator += "\n    }\n)"
        else:
            decorator = "@collection(tag_name='{tag_name}')".format(tag_name=name)

        return decorator
