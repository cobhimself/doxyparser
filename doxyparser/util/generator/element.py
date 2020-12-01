from xml.etree.ElementTree import tostring
import pyinputplus
import textwrap
import inflect
from .super import Super
from ..wrap import wrap, wrapxml

class Element(Super):
    def __init__(self, element, node_type):
        self._type = node_type
        self._attr = {}
        super().__init__(element)

    def get_name(self):
        return self._definition.name

    def get_content(self):
        return self.get_type().get_content()

    def is_element_only(self):
        return self.get_type().is_element_only()

    def is_multiple(self):
        return self.get_type().is_multiple()

    def is_simple(self):
        return self.get_type().is_simple()

    def is_text_only(self):
        return self.get_type().is_text_only()

    def allows_elements_and_text(self):
        return self.get_type().has_mixed_content()

    def get_type(self):
        return self._type

    def get_attributes(self):
        if len(self._attr) == 0:
            from .attribute import Attribute
            for attr_name, attr in self._definition.attributes.items():
                self._attr[attr_name] = Attribute(attr)

        return self._attr

    def get_attribute_by_name(self, name):
        return self._attr.get(name, None)

    def get_decorator(self):
        attributes = self.get_attributes().values()
        parent = self._definition.parent.parent.name
        type_name = self.get_type().get_name()
        name = self.get_name()

        if self.is_simple():
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

    def get_as_class(self):
        name = self.get_name()
        node_type = self.get_type().get_name()
        type_module_name = node_type.lower()

        code = "from ...node import Node\n"
        code += "from ...decorators import tag\n"
        code += f"from ..types.{type_module_name} import {node_type}\n"
        code += "\n"
        code += f"@tag('{name}')\n"
        code += f"class {name.title()}({node_type}):\n"

        class_comment = f'"""Model representation of a doxygen {name} element' + "\n\n"
        class_comment += "XSD for this element:\n\n"
        class_comment += wrapxml(self._definition.schema_elem) + "\n"

        if self._definition.parent is not None:
            class_comment += "Parent XSD:\n\n"
            class_comment += wrapxml(self._definition.parent.schema_elem) + "\n"

        class_comment += '"""'

        code += wrap(class_comment, '    ', '    ')

        #final new line
        code += "\n"

        return code
