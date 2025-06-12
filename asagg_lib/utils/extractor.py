from abc import ABC, abstractmethod
from inspect import getmembers
from typing import List

from asagg_lib.typing.generics import ClassType


class Extractor(ABC):
    """
    This class is a utility class to extract **private** and **protected** attributes

    Methods:
        extract_attributes(_class):
            this methods extract all attributes and return a list with all attributes names

        extract_name_of_class(_class):
            this methods return a name of _class
    """

    @abstractmethod
    def __init__(self):
        pass

    @staticmethod
    def extract_attributes(_class: ClassType) -> List[str]:
        """
        Extract all attributes **private** and **protected** of class passed as argument

        Parameters:
            _class: Class that's you want extract the attributes

        Returns:
            List with all **private** and **protected** attributes

        Examples:
            >>> class T:
            ...     def __init__(self):
            ...         self._test = "protected_attribute"
            ...
            >>> Extractor.extract_attributes(T)
            ['_test']
        """
        attributes = []
        for member in getmembers(_class):
            if member[0] == "__init__":
                attributes = member[1].__code__.co_names
                break

        return list(attributes)

    @staticmethod
    def extract_name_of_class(_class: ClassType) -> str:
        """
        Extract name of the class passed

        Parameters:
            _class: Class that's you want extract the name

        Returns:
            Name of class

        Examples:
            >>> Extractor.extract_name_of_class(Extractor)
            'Extractor'
        """
        return _class.__name__
