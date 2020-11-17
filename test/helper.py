import textwrap
import pathlib
import yaml

from doxyparser.parser import Parser
from doxyparser.loader import Loader
from .output import Output

TEST_DIR = str(pathlib.Path(__file__).parent.resolve()) + '/'
SAMPLE_DATA_DIR = TEST_DIR + '_sample_data'
EXPECTATION_DATA_DIR = TEST_DIR + '_expectation_data'
DOXYGEN_BUILD_DIR = SAMPLE_DATA_DIR + '/_build/php/xml'

out = Output(2)

_wrapper = textwrap.TextWrapper(width=120)


def get_doxygen_build_dir():
    return DOXYGEN_BUILD_DIR


def get_parser():
    try:
        parser
    except NameError:
        parser = Parser(Loader(get_doxygen_build_dir()))

    return parser


def get_data_provider(path, inside=None):
    expectation_path = EXPECTATION_DATA_DIR + '/' + path
    if not pathlib.Path(expectation_path).exists():
        raise Exception(
            'Attempted to load non-existant expectation data file "' + expectation_path + '"'
        )

    stream = open(expectation_path, 'r')

    parsed = yaml.safe_load(stream)
    if inside is not None:
        parsed = parsed[inside]

    # Convert the data provider into parameterized tuples
    return [(key, parsed[key]) for key in parsed]


def _make_assertion_for_sub_confirmation(
    node,
    expected_value,
    value_getter
):
    for confirmation in expected_value.keys():
        expected = expected_value[confirmation]
        if confirmation == 'count':
            actual = len(value_getter())
            out.puts(['assert', 'count -> ', expected, ' == ', actual])
            assertion = 'value is {} {} (actual {} {})'.format(
                type(expected),
                expected,
                type(actual),
                actual
            )
            assert expected == actual, assertion
        elif confirmation == 'empty':
            actual = value_getter()._node.text.strip()
            out.puts(['assert', 'empty -> "', actual, '"'])
            assert actual == '', 'text node is empty'
        elif confirmation == 'children':
            out.inc()
            confirm_node_expectations(
                node,
                expected['getter'],
                expected['expectations']
            )
            out.dec()
        else:
            raise Exception('Unknown confirmation "' + confirmation + '"')


def confirm_node_expectations(
    class_under_test,
    node_getter,
    expectations,
):
    try:
        out.puts(
            ['Confirming', class_under_test]
        )

        out.inc()

        # This method will return all of the nodes we are targeting with the test
        node_getter = 'get_' + node_getter

        out.puts(
            ['Node getter', node_getter]
        )

        # Get the list of nodes associated with our get method
        try:
            nodes = getattr(class_under_test, node_getter)()
        except AttributeError as err:
            raise Exception(
                'Node getter "' + node_getter +
                '" does not exist in ' + str(class_under_test)
            ) from err

        if type(nodes) is list:
            out.puts(
                ['Num nodes', len(nodes)],
                ['assert', len(expectations), ' == ', len(nodes)]
            )

            # We need to know if we have the same lengths!
            assert len(expectations) == len(
                nodes), 'Retrieved node count matches expectations'

        index = 0

        for node_expectations in expectations:
            node = nodes if not isinstance(nodes, list) else nodes[index]

            out.puts(
                ['node #' + str(index), node]
            )

            out.inc()

            out.puts(
                ['expect', node_expectations],
            )

            out.inc()

            # Our node_expectations consist of a getter_method key and expected value
            for value_getter, expected_value in node_expectations.items():

                try:
                    val_getter = getattr(node, 'get_' + value_getter)
                except AttributeError as err:
                    raise Exception(
                        'Value getter "get_' + value_getter +
                        '" does not exist in ' + str(node)
                    ) from err

                # Are we making a sub assertion in our expectation data?
                if type(expected_value) is dict:
                    _make_assertion_for_sub_confirmation(
                        node,
                        expected_value,
                        val_getter,
                    )
                else:
                    expected_value = str(expected_value)
                    actual_value = val_getter()
                    out.puts(
                        ['assert', 'get_' + value_getter + ' -> ',
                            expected_value, ' == ', actual_value]
                    )
                    assertion = 'get_{} returns {} {} (actual: {} {})'.format(
                        value_getter,
                        type(expected_value),
                        expected_value,
                        type(actual_value),
                        actual_value
                    )
                    assert expected_value == actual_value, assertion

            index += 1
            out.dec()
            out.dec()
    except Exception as err:
        raise err
    finally:
        out.dump()
