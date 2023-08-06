import importlib
import inspect
import re
import os
from typing import Any, Callable, Type, Union, get_type_hints

from pydantic import BaseModel, parse_raw_as
from pydantic.tools import parse_obj_as


def name_to_title(name: str) -> str:
    """Converts a camelCase or snake_case name to title case."""
    # If camelCase -> convert to snake case
    name = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    name = re.sub("([a-z0-9])([A-Z])", r"\1_\2", name).lower()
    # Convert to title case
    return name.replace("_", " ").strip().title()


def is_compatible_type(type: Type) -> bool:
    """Returns `True` if the type is workcell-compatible."""
    try:
        if issubclass(type, BaseModel):
            return True
    except Exception:
        pass

    try:
        # valid list type
        if type.__origin__ is list and issubclass(type.__args__[0], BaseModel):
            return True
    except Exception:
        pass

    return False


def get_input_type(func: Callable) -> Type:
    """Returns the input type of a given function (callable).

    Args:
        func: The function for which to get the input type.

    Raises:
        ValueError: If the function does not have a valid input type annotation.
    """
    type_hints = get_type_hints(func)

    if "input" not in type_hints:
        raise ValueError(
            "The callable MUST have a parameter with the name `input` with typing annotation. "
            "For example: `def my_workcell(input: InputModel) -> OutputModel:`."
        )

    input_type = type_hints["input"]

    if not is_compatible_type(input_type):
        raise ValueError(
            "The `input` parameter MUST be a subclass of the Pydantic BaseModel or a list of Pydantic models."
        )

    # TODO: return warning if more than one input parameters

    return input_type


def get_output_type(func: Callable) -> Type:
    """Returns the output type of a given function (callable).

    Args:
        func: The function for which to get the output type.

    Raises:
        ValueError: If the function does not have a valid output type annotation.
    """
    type_hints = get_type_hints(func)
    if "return" not in type_hints:
        raise ValueError(
            "The return type of the callable MUST be annotated with type hints."
            "For example: `def my_workcell(input: InputModel) -> OutputModel:`."
        )

    output_type = type_hints["return"]

    if not is_compatible_type(output_type):
        raise ValueError(
            "The return value MUST be a subclass of the Pydantic BaseModel or a list of Pydantic models."
        )

    return output_type


def format_workcell_path(import_string: str) -> str:
    """Format a workcell path from an string.
    Args: 
        import_string, str
        split workcell_path into project_name and function_name
        e.g. import_string = "app.py"
        e.g. import_string = "./app.py"
        e.g. import_string = "examples/hello_world/app.py"
    Returns:
        workcell_path, str
        e.g. workcell_path = "examples.hello_world.app"
    """
    if not os.path.exists(import_string):
        raise ValueError("The callable path MUST be a valid path. Import string: {}".format(import_string))
    if os.path.basename(import_string) != "app.py":
        raise ValueError("The callable function MUST be named as app.py, now is named as : {}".format(os.path.basename(import_string)))
    workcell_path = import_string.replace("/", ".")[:-3]
    return workcell_path


def get_callable(import_string: str) -> Callable:
    """Import a callable from an string."""
    # e.g. import_string = "examples.hello_world.app"
    # validation
    import_string = format_workcell_path(import_string)
    try:
        mod = importlib.import_module(import_string)
        func = getattr(mod, "main")
    except:
        raise ValueError("The callable path MUST specify the function file. Import string: {}".format(import_string))
    return func


def format_workcell_name(workcell_path: str) -> str:
    """Format a workcell_name from an workcell_path.
    Args: 
        workcell_path, str
        split workcell_path into workcell_name
        e.g. workcell_path = "examples.hello_world.app"
    Returns:
        workcell_name, str
        remove prefix/suffix, replace "_" with "-"
        e.g. workcell_name = "hello-world"
    """
    workcell_name = workcell_path.split(".")[-2].replace("_", "-")
    return workcell_name


class Workcell:
    def __init__(self, func: Union[Callable, str]) -> None:
        if isinstance(func, str):
            # Try to load the function from a string notion
            self.function = get_callable(func)
        else:
            self.function = func

        self._name = "workcell"
        self._version = "0.0.2" # TODO: workcell function's version should be passed when init.
        self._description = ""
        self._root_path = "/" # can be adjusted if behind proxy server        
        self._input_type = None
        self._output_type = None

        if not callable(self.function):
            raise ValueError("The provided function parameters is not a callable.")

        if inspect.isclass(self.function):
            raise ValueError(
                "The provided callable is an uninitialized Class. This is not allowed."
            )

        if inspect.isfunction(self.function):
            # The provided callable is a function
            self._input_type = get_input_type(self.function)
            self._output_type = get_output_type(self.function)

            try:
                # Get name
                self._name = name_to_title(self.function.__name__)
            except Exception:
                pass

            try:
                # Get description from function
                doc_string = inspect.getdoc(self.function)
                if doc_string:
                    self._description = doc_string
            except Exception:
                pass
            
        elif hasattr(self.function, "__call__"):
            # The provided callable is a function
            self._input_type = get_input_type(self.function.__call__)  # type: ignore
            self._output_type = get_output_type(self.function.__call__)  # type: ignore

            try:
                # Get name
                self._name = name_to_title(type(self.function).__name__)
            except Exception:
                pass

            try:
                # Get description from
                doc_string = inspect.getdoc(self.function.__call__)  # type: ignore
                if doc_string:
                    self._description = doc_string

                if (
                    not self._description
                    or self._description == "Call self as a function."
                ):
                    # Get docstring from class instead of __call__ function
                    doc_string = inspect.getdoc(self.function)
                    if doc_string:
                        self._description = doc_string
            except Exception:
                pass
        else:
            raise ValueError("Unknown callable type.")

    @property
    def name(self) -> str:
        return self._name
    
    @property
    def version(self) -> str:
        return self._version
    
    @property
    def description(self) -> str:
        return self._description
    
    @property
    def root_path(self) -> str:
        return self._root_path    

    @property
    def input_type(self) -> Any:
        return self._input_type

    @property
    def output_type(self) -> Any:
        return self._output_type

    def __call__(self, input: Any, **kwargs: Any) -> Any:

        input_obj = input

        if isinstance(input, str):
            # Allow json input
            input_obj = parse_raw_as(self.input_type, input)

        if isinstance(input, dict):
            # Allow dict input
            input_obj = parse_obj_as(self.input_type, input)

        return self.function(input_obj, **kwargs)
