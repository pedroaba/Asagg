import unittest

from asagg_lib.asagg import Asagg


class TestAsaggSetter(unittest.TestCase):
    def setUp(self):
        self.expected_values = _expect = {
            "_edge": 10,
            "_edge_after": 20,
            "_foo": 12,
            "_foo_after": 321,
        }

        @Asagg.setter
        class Square:
            def __init__(self):
                self._edge = _expect["_edge"]
                self._foo = _expect["_foo"]

        self.square = Square()

    def test_it_should_be_able_to_create_setter_to_private_and_protected_properties(
        self,
    ):
        list_of_the_members = self.square.__dir__()

        self.assertIn("edge", list_of_the_members)
        self.assertIn("foo", list_of_the_members)

    def test_it_should_be_able_to_set_a_value_to_new_setter_property(self):
        self.square.edge = self.expected_values["_edge_after"]
        self.square.foo = self.expected_values["_foo_after"]
        self.assertEqual(self.expected_values["_edge_after"], self.square._edge)
        self.assertEqual(self.expected_values["_foo_after"], self.square._foo)

    def test_it_should_not_be_able_to_set_a_value_to_new_setter_property(self):
        with self.assertRaises(TypeError):
            self.square.edge = "Should be faield"
