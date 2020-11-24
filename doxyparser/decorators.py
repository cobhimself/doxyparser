from .loader import Loader

COLLECTIONS = 'collections'
COLLECTORS = 'collectors'
XPATH = 'xpath'
TAG = 'tag'

def collection(tag_name, xpath, collectors=None):
    def add_map(cls):
        define_meta(cls)
        # Make sure we have a collection ready
        if get_meta(cls, COLLECTIONS) is None:
            set_meta(cls, COLLECTIONS, {})

        meta = get_meta(cls)

        # Add the collection xpath for the tag
        meta[COLLECTIONS][tag_name] = {'path': xpath}

        #Add our collector methods
        if collectors is not None:
            for getter, args in collectors.items():
                if meta[COLLECTIONS][tag_name].get(COLLECTORS) is None:
                    meta[COLLECTIONS][tag_name][COLLECTORS] = {}

                meta[COLLECTIONS][tag_name][COLLECTORS][getter] = args

        _add_collection_methods(cls)

        return cls

    return add_map

def _add_collection_methods(cls):
    def getter(fn_name, coll_tag, xpath_args=None):
        def collect(self):
            return self.get_collection(coll_tag, xpath_args)
        collect.__name__ = fn_name
        return collect

    main_doc_template = 'Return child {tag} elements'
    collection_doc_template = main_doc_template + ' matching xpath "{tag}/[{filters}]"'
    return_template = """

    Returns:
        list({returns}): A list of {tag} elements found.
    """

    collections = get_meta(cls, COLLECTIONS)
    for coll_tag in collections.keys():
        xsd = cls.__module__.split('.')[1]
        tag_class = Loader.load_tag_class(xsd, coll_tag)
        curr_collection = collections[coll_tag]
        collectors = curr_collection.get(COLLECTORS)

        #Our main collection tag should have a method where all elements
        #matching the tag name are returned. This method will not use any
        #xpath arguments and will simply return all elements matching the
        #tag name.
        fn_name = 'get_{}s'.format(coll_tag)
        get = getter(fn_name, coll_tag)
        get.__doc__ = main_doc_template + return_template.format(
            tag=coll_tag,
            returns='.'.join([tag_class.__module__, tag_class.__name__])
        ).strip()
        setattr(cls, fn_name, get)

        if collectors:
            for method_tail, xpath_args in collectors.items():
                fn_name = 'get_{}_{}'.format(coll_tag, method_tail)
                get = getter(fn_name, coll_tag, xpath_args)
                get.__doc__ = collection_doc_template + return_template.format(
                    tag=coll_tag,
                    filters= ', '.join(['@' + key + '=' +value for key, value in xpath_args.items()]),
                    returns='.'.join([tag_class.__module__, tag_class.__name__])
                ).strip()
                setattr(cls, fn_name , get)

def tag(tag_name):
    def add_tag(cls):
        define_meta(cls)
        set_meta(cls, TAG, tag_name)

        return cls

    return add_tag

def define_meta(cls):
    if getattr(cls, '_meta', None) is None:
        setattr(cls, '_meta', {})

def get_meta(cls, key = None):
    meta = getattr(cls, '_meta', None)

    if None is key:
        return meta

    if None is not meta:
        return meta.get(key)

    return None

def set_meta(cls, key, value):
    meta = get_meta(cls)

    meta[key] = value
