def format_attributes_names(
    attributes: list[str], classname: str = ""
) -> list[str]:
    """Format attribute names by cleaning mangled prefixes.

    Parameters:
        attributes: list[str]
            List of attribute names to format.
        classname: str
            Optional class name used when removing mangled prefixes.

    Returns:
        list[str]:
            A list containing the formatted attribute names.

    Examples:
        >>> format_attributes_names(["_foo", "_Square_foo"], "Square")
        ['foo', 'foo']
    """
    attributes_formatted: list[str] = []
    for attr in attributes:
        # remove leading underscores that mark protected or private members
        attr = attr.lstrip("_")

        # handle Python name mangling for private attributes by removing the
        # class name if it is present at the start of the attribute
        if classname and attr.startswith(classname):
            attr = attr[len(classname) :]
            # after removing the class name there may still be a leading
            # underscore left from the mangling
            attr = attr.lstrip("_")

        attributes_formatted.append(attr)

    return attributes_formatted
