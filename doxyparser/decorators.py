from types import MethodType
from .loader import Loader
import textwrap

COLLECTIONS = 'collections'
COLLECTORS = 'collectors'
XPATH = 'xpath'
TAG = 'tag'

def collection(tag_name, xpath, collectors={}):
    def add_map(cls):
        define_meta(cls)
        # Make sure we have a collection ready
        if cls._meta.get(COLLECTIONS) is None:
            cls._meta[COLLECTIONS] = {}

        # Add the collection xpath for the tag
        cls._meta[COLLECTIONS][tag_name] = {'path': xpath}

        #Add our collector methods
        for getter, args in collectors.items():
            if cls._meta[COLLECTIONS][tag_name].get(COLLECTORS) is None:
                cls._meta[COLLECTIONS][tag_name][COLLECTORS] = {}

            cls._meta[COLLECTIONS][tag_name][COLLECTORS][getter] = args

        _add_collection_methods(cls)

        return cls

    return add_map

def _add_collection_methods(cls):
    def getter(cls, fn_name, tag, xpath_args=None):
        def collect(self):
            return self.get_collection(tag, xpath_args)
        collect.__name__ = fn_name
        return collect

    main_doc_template = 'Return child {tag} elements'
    collection_doc_template = main_doc_template + ' matching xpath "{tag}/[{filters}]"'
    return_template = """

    Returns:
        list({returns}): A list of {tag} elements found.
    """
    for tag in cls._meta[COLLECTIONS].keys():
        xsd = cls.__module__.split('.')[1]
        tag_class = Loader.load_tag_class(xsd, tag)
        curr_collection = cls._meta[COLLECTIONS][tag]
        collectors = curr_collection.get(COLLECTORS)

        #Our main collection tag should have a method where all elements
        #matching the tag name are returned. This method will not use any
        #xpath arguments and will simply return all elements matching the
        #tag name.
        fn_name = 'get_{}s'.format(tag)
        get = getter(cls, fn_name, tag)
        get.__doc__ = main_doc_template + return_template.format(
            tag=tag,
            returns='.'.join([tag_class.__module__, tag_class.__name__])
        ).strip()
        setattr(cls, fn_name, get)

        if collectors:
            for method_tail, xpath_args in collectors.items():
                fn_name = 'get_{}_{}'.format(tag, method_tail)
                get = getter(cls, fn_name, tag, xpath_args)
                get.__doc__ = collection_doc_template + return_template.format(
                    tag=tag,
                    filters= ', '.join(['@' + key + '=' +value for key, value in xpath_args.items()]),
                    returns='.'.join([tag_class.__module__, tag_class.__name__])
                ).strip()
                setattr(cls, fn_name , get)

def tag(tag_name):
    def add_tag(cls):
        define_meta(cls)
        cls._meta[TAG] = tag_name
        return cls

    return add_tag

def define_meta(cls):
    if getattr(cls, '_meta', None) is None:
        setattr(cls, '_meta', {})
