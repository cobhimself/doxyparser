import pytest
import pathlib
import yaml
from doxyparser.parser import Parser

_test_dir = str(pathlib.Path(__file__).parent.resolve()) + '/'
_sample_data_dir = _test_dir + 'sample_data'
_expectation_data_dir = _test_dir + 'expectation_data'
_doxygen_build_dir = _sample_data_dir + '/_build/php/xml'
_parser = None


def get_doxygen_build_dir():
    return _doxygen_build_dir


def get_parser():
    try:
        _parser
    except NameError:
        _parser = Parser(get_doxygen_build_dir())

    return _parser


def get_data_provider(path, inside=None):
    stream = open(_expectation_data_dir + '/' + path, 'r')
    parsed = yaml.safe_load(stream)
    if None != inside:
        parsed = parsed[inside]

    # Convert the data provider into parameterized tuples
    return [(key, parsed[key]) for key in parsed]


def _get_values_for_dp_confirmation(expected_value, value_getter):
    confirmation = list(expected_value.keys())[0]
    if confirmation == 'count':
        return (expected_value[confirmation], len(value_getter()))
    else:
        raise Exception('Unknown confirmation "' + confirmation + '"')


def confirm_node_expectations(
    class_under_test,
    node_getter,
    expectations,
):
    # This method will return all of the nodes we are targeting with the test
    node_getter = 'get_' + node_getter
    print('> Node getter: ' + node_getter)
    print('> Expectations: ', expectations)

    # Get the list of nodes associated with our get method
    nodes = getattr(class_under_test, node_getter)()

    print('> Node count:', len(nodes))

    # We need to know if we have the same lengths!
    assert len(nodes) == len(expectations)

    index = 0

    for node_expectations in expectations:
        print('> Current Node Expectations: ', node_expectations)
        # Our node_expectations consist of a getter_method key and expected value
        for value_getter, expected_value in node_expectations.items():
            node = nodes[index]

            print('    index: ', index)
            print('    node: ', node)

            value_getter = getattr(node, 'get_' + value_getter)

            print('    getter: ', value_getter)

            if (type(expected_value) == dict):
                (expected_value, actual_value) = _get_values_for_dp_confirmation(
                    expected_value, value_getter)
            else:
                actual_value = value_getter()

            print('    Checking ', expected_value, ' === ', actual_value)

            assert expected_value == actual_value

        index += 1
