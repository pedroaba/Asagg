import unittest

from asagg_lib.utils.formatter import format_attributes_names


class TestFormatter(unittest.TestCase):
    def setUp(self):
        super(TestFormatter, self).setUp()
        self.attributes = ["_foo", "_Square_foo"]

    def test_it_should_be_able_to_format_privates_and_protected_attributes(
        self,
    ):
        attributes_formatteds = format_attributes_names(
            self.attributes, classname="Square"
        )

        self.assertEqual(attributes_formatteds, ["foo", "foo"])

    def test_it_should_preserve_middle_underscores(self):
        attributes = ["_my_private_attr", "_Square_my_private_attr"]
        attributes_formatteds = format_attributes_names(
            attributes, classname="Square"
        )

        self.assertEqual(
            attributes_formatteds, ["my_private_attr", "my_private_attr"]
        )

    def test_it_should_not_format_attributes_without_classname(
        self,
    ):
        attributes_formatteds = format_attributes_names(self.attributes)

        self.assertEqual(attributes_formatteds, ["foo", "Square_foo"])
