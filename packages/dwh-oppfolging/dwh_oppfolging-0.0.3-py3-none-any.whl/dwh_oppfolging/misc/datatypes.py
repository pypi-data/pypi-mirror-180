# import dataclasses
from typing import Callable


__doc__ = "Sub-module for data types"


class TransformedEntry:
    """returns a dict with a transformed un-nested entry when called"""

    def __init__(
        self,
        path_in: str,
        path_out: str = "",
        allow_missing: bool = True,
        transform: Callable = lambda x: x,
    ) -> None:
        self.path_in = path_in.split(".")
        self.path_out = path_out if path_out else "_".join(path_in)
        self.allow_missing = allow_missing
        self.transform = transform

    def __call__(self, input_data: dict):
        input_value = None
        try:
            for subpath in self.path_in:
                input_value = input_data[subpath]
        except KeyError:
            if not self.allow_missing:
                raise
        output_value = self.transform(input_value)
        output_data = {}
        last = output_data
        for subpath in self.path_out:
            last[subpath] = {}
        last[subpath] = output_value
        return output_data
