import pytest
import pathlib
import yaml
from doxyparser.parser import Parser
from clint.textui import puts, indent
from doxyparser.loader import Loader

_test_dir = str(pathlib.Path(__file__).parent.resolve()) + '/'
_sample_data_dir = _test_dir + '_sample_data'
_expectation_data_dir = _test_dir + '_expectation_data'
_doxygen_build_dir = _sample_data_dir + '/_build/php/xml'
_parser = None


def debug(ind=0, prefix='', out=[]):
    with indent(ind, quote=prefix):
        for content in out:
            content[0] = '[' + content[0] + ']: '
            # Convert non-strings to strings
            puts(' '.join(str(item).strip() for item in content))


def get_doxygen_build_dir():
    return _doxygen_build_dir


def get_parser():
    try:
        _parser
    except NameError:
        _parser = Parser(Loader(get_doxygen_build_dir()))

    return _parser


def get_data_provider(path, inside=None):
    stream = open(_expectation_data_dir + '/' + path, 'r')
    parsed = yaml.safe_load(stream)
    if None != inside:
        parsed = parsed[inside]

    # Convert the data provider into parameterized tuples
    return [(key, parsed[key]) for key in parsed]


def _make_assertion_for_sub_confirmation(
    node,
    expected_value,
    value_getter,
    debug_ind
):
    for confirmation in expected_value.keys():
        expected = expected_value[confirmation]
        if confirmation == 'count':
            assert expected == len(value_getter())
        elif confirmation == 'children':
            confirm_node_expectations(
                node,
                expected['getter'],
                expected['expectations'],
                debug_ind + 2
            )
        else:
            raise Exception('Unknown confirmation "' + confirmation + '"')


def confirm_node_expectations(
    class_under_test,
    node_getter,
    expectations,
    debug_ind=0
):
    debug(ind=debug_ind, prefix='>', out=[
        ['Confirming node expectations']
    ])

    debug_ind += 2

    # This method will return all of the nodes we are targeting with the test
    node_getter = 'get_' + node_getter

    debug(ind=debug_ind, out=[
        ['Node getter', node_getter],
        ['Expectations', expectations]
    ])

    # Get the list of nodes associated with our get method
    nodes = getattr(class_under_test, node_getter)()

    debug(ind=debug_ind, out=[
        ['Node count', len(nodes)]
    ])

    # We need to know if we have the same lengths!
    assert len(nodes) == len(expectations)

    index = 0

    debug_ind += 2

    for node_expectations in expectations:
        debug(ind=debug_ind, out=[
            ['Current Node Expectations', node_expectations]
        ])
        # Our node_expectations consist of a getter_method key and expected value
        for value_getter, expected_value in node_expectations.items():
            node = nodes[index]

            debug(ind=debug_ind + 2, out=[
                ['index', index],
                ['node', node]
            ])

            value_getter = getattr(node, 'get_' + value_getter)

            debug(ind=debug_ind + 2, out=[
                ['getter', value_getter]
            ])

            # Are we making a sub assertion in our expectation data?
            if (type(expected_value) == dict):
                _make_assertion_for_sub_confirmation(
                    node,
                    expected_value,
                    value_getter,
                    debug_ind
                )
            else:
                actual_value = value_getter()
                debug(ind=debug_ind + 2, out=[
                    ['Checking ', expected_value, ' === ', actual_value]
                ])
                assert expected_value == actual_value

        index += 1
