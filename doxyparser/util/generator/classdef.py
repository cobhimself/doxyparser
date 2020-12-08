from ..wrap import wrap

class ClassDef():
    def __init__(self, name):
        self._name = name
        self._import_lines = []
        self._decorators = []
        self._doc = ''
        self._super = None

    def add_import(self, import_line):
        self._import_lines.append(import_line)

    def get_imports(self):
        return "\n".join(self._import_lines)

    def extends(self, name):
        self._super = name

    def add_decorator(self, decorator):
        self._decorators.append(decorator)

    def get_decorators(self):
        return "\n".join(self._decorators)

    def set_class_doc(self, doc):
        self._doc = doc

    def get_class_doc(self):
        return wrap('"""' + self._doc + "\n" + '"""', '    ', '    ')

    def get(self):
        pass

    def __str__(self):
        out = self.get_imports() + "\n\n"
        out += self.get_decorators() + "\n"
        out += f"class {self._name.title()}({self._super}):\n"
        out += self.get_class_doc()

        return out
