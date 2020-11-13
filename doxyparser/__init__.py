TAG_MAP = {
    'index': {
        'doxygenindex': 'DoxygenIndex',
        'compound': 'Compound',
        'member': 'Member'
    }
}

for xsd_name, xsd in TAG_MAP.items():
    for tag, class_name in xsd.items():
        TAG_MAP[xsd_name][tag] = '.'.join([
            'doxyparser',
            xsd_name,
            'types',
            tag,
            class_name
        ])
