from abc import ABC, abstractmethod
from typing import Any

from asagg_lib.typing.generics import _T
from asagg_lib.utils.extractor import Extractor
from asagg_lib.utils.formatter import format_attributes_names
from asagg_lib.utils.validators import validate_type_comparing_with_annother_var


class Asagg(ABC):
    """
    An abstract base class for generating getters and setters for private and protected attributes.
    This class provides methods to generate getters for private and protected attributes of a given class.

    Methods:
        __init__
            This is an abstract method that must be implemented by subclasses.
        data(_class):
            A static method that returns the input class '_class' with getters and setters generateds.

        getter(_class):
            A static method that generates getters for private and protected attributes for the input class '_class'.

        setter(_class):
            A static method that generates setters for private and protected attributes for the input class '_class'.

        _default_getter(attr):
            A static method that returns a default getter for the specified attribute 'attr'.

        _default_setter(attr):
            A static method that returns a default setter for the specified attribute 'attr'.

        __default_function_setter(self, attr, value):
            A static method that controls when is able to set a value on 'attr'.
    """

    @abstractmethod
    def __init__(self):
        """Abstract method"""
        pass

    @staticmethod
    def data(_class: _T) -> _T:
        """
        Generate Getters and Setters for all **private** and **protected** attributes for '_class', this method modify
        the class structure to generate a getter  and setters, adding new functions and properties

        Parameters:
            _class: this parameter is a class that will be generated the getters and setters

        Returns:
            The return is the same class, but the class has getters and setters for private and protected attributes
        """
        attrs = Extractor.extract_attributes(_class)
        classname = Extractor.extract_name_of_class(_class)

        new_attributes = []
        for index, (attr_raw, attr_formatted) in enumerate(
            zip(attrs, format_attributes_names(attrs, classname))
        ):
            value_of_property = Asagg._default_getter_and_setter(attr_raw)

            setattr(_class, attr_formatted, value_of_property)
            new_attributes.append(attr_formatted)
            del value_of_property

        for new_attr in new_attributes:
            _class.__annotations__[new_attr] = type(getattr(_class, new_attr))

        return _class

    @staticmethod
    def getter(_class: _T) -> _T:
        """
        Generate Getters for all **private** and **protected** attributes for '_class', this method modify the class
        structure to generate a getter, adding new functions and properties

        Parameters:
            _class: this parameter is a class that will be generated the getters

        Returns:
            The return is the same class, but the class has getters for private and protected attributes
        """
        attrs = Extractor.extract_attributes(_class)
        classname = Extractor.extract_name_of_class(_class)

        new_attributes = []
        for attr_raw, attr_formatted in zip(
            attrs, format_attributes_names(attrs, classname)
        ):
            value_of_property: property = Asagg._default_getter(attr_raw)

            setattr(_class, attr_formatted, value_of_property)
            new_attributes.append(attr_formatted)

            del value_of_property

        for new_attr in new_attributes:
            _class.__annotations__[new_attr] = type(getattr(_class, new_attr))

        return _class

    @staticmethod
    def setter(_class: _T) -> _T:
        """
        Generate Setters for all **private** and **protected** attributes for '_class', this method modify the class
        structure to generate a setter, adding new functions and properties

        Parameters:
            _class: this parameter is a class that will be generated the setters

        Returns:
            The return is the same class, but the class has getters for private and protected attributes
        """
        attrs = Extractor.extract_attributes(_class)
        classname = Extractor.extract_name_of_class(_class)

        new_attributes = []
        for attr_raw, attr_formatted in zip(
            attrs, format_attributes_names(attrs, classname)
        ):
            value_of_property: property = Asagg._default_setter(attr_raw)

            setattr(_class, attr_formatted, value_of_property)
            new_attributes.append(attr_formatted)

            del value_of_property

        for new_attr in new_attributes:
            _class.__annotations__[new_attr] = type(getattr(_class, new_attr))

        return _class

    @staticmethod
    def _default_getter(attr: Any) -> property:
        """
        This function is an alias to create a default getter for any attr

        Parameters:
            attr: any attribute of a class to create a property function

        Returns:
            a property function for the attribute
        """
        return property(lambda self: getattr(self, attr))

    @staticmethod
    def _default_setter(attr: Any) -> property:
        """
        This function is an alias to create a default setter for any attr

        Parameters:
            attr: any attribute of a class to create a property function

        Returns:
            a property function for the attribute
        """
        return property(
            fset=lambda self, value: Asagg.__default_function_setter(
                self, attr, value
            )
        )

    @staticmethod
    def _default_getter_and_setter(attr):
        """
        This function is an alias to create a default setter and getter for any attr

        Parameters:
            attr: any attribute of a class to create a property function

        Returns:
            a property function for the attribute
        """
        return property(
            lambda self: Asagg.__default_function_getter(self, attr),
            lambda self, value: Asagg.__default_function_setter(
                self, attr, value
            ),
        )

    @staticmethod
    def __default_function_setter(self: object, attr: str, value: Any) -> None:
        """
        This method is responsible for setting the value on the object

        Parameters:
            self: Object that you want to create a set function
            attr: attribute of the Object
            value: value that you want to set in attribute

        Returns:

        """
        type_to_compare = type(getattr(self, attr))

        if validate_type_comparing_with_annother_var(type_to_compare, value):
            setattr(self, attr, value)
            return
        raise TypeError(
            f"type of {self}.{attr} is different of {value} | "
            f"TypeObject = {getattr(self, attr)} & TypeValue = {type(value)}"
        )

    @staticmethod
    def __default_function_getter(self: Any, attr: str) -> Any:
        """
        This method is responsible for getting the value from the object

        Parameters:
            self: Object that you want to create a set function
            attr: attribute of the Object

        Returns:
            value of attribute
        """
        return getattr(self, attr)
