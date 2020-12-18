from .decorator import Decorator
from ..loader import Loader

COLLECTIONS = 'collections'
COLLECTORS = 'collectors'

class Collection(Decorator):
    def __init__(self, tag_name, xpath, collectors=None):
        super().__init__()
        self._tag_name = tag_name
        self._xpath = xpath
        self._collectors = collectors if collectors is not None else {}

    def do(self):
        self._add_tag_collection()
        self._add_collection_methods()

    def _add_tag_collection(self):
        # Make sure we have a collection ready
        collections = self.provide(self.get_meta(), COLLECTIONS, {})

        # Add the collection xpath for the tag
        tag_collection = self.provide(collections, self._tag_name, {'path': self._xpath})

        #Add our collector methods
        if self._collectors is not None:
            for getter, args in self._collectors.items():
                tag_collectors = self.provide(tag_collection, COLLECTORS, {})
                tag_collectors[getter] = args

    @staticmethod
    def _getter(fn_name, coll_tag, xpath_args=None):
        def collect(self):
            return self.get_collection(coll_tag, xpath_args)
        collect.__name__ = fn_name

        return collect

    def _get_collections(self):
        return self.get_meta(COLLECTIONS)

    def _add_collection_methods(self):
        main_doc_template = 'Return child {tag} elements'
        collection_doc_template = main_doc_template + ' matching xpath "{tag}/[{filters}]"'
        return_template = """

        Returns:
            list({returns}): A list of {tag} elements found.
        """

        xsd = self.get_xsd_from_cls()
        coll_tag = self._tag_name
        tag_class = Loader.load_tag_class(xsd, coll_tag)
        collectors = self._collectors

        main_doc_template = f'Return child {coll_tag} elements'
        collection_doc_template = main_doc_template + ' matching xpath "{tag}/[{filters}]"'
        return_template = """

        Returns:
            list({returns}): A list of {tag} elements found.
        """

        #Our main collection tag should have a method where all elements
        #matching the tag name are returned. This method will not use any
        #xpath arguments and will simply return all elements matching the
        #tag name.
        fn_name = f'get_{coll_tag}s'
        doc = main_doc_template + return_template.format(
            tag=coll_tag,
            returns='.'.join([tag_class.__module__, tag_class.__name__])
        )
        self.add_method_to_cls(fn_name, self._getter(fn_name, coll_tag), doc)

        if collectors:
            for method_tail, xpath_args in collectors.items():
                fn_name = f'get_{coll_tag}_{method_tail}'
                get = self._getter(fn_name, coll_tag, xpath_args)
                doc = collection_doc_template + return_template.format(
                    tag=coll_tag,
                    filters= ', '.join([f'@{key}={value}' for key, value in xpath_args.items()]),
                    returns='.'.join([tag_class.__module__, tag_class.__name__])
                ).strip()
                self.add_method_to_cls(fn_name, get, doc)
