import typing

from dataclasses import dataclass


@dataclass
class SymbolTable:
    table: typing.MutableSequence[str]

    def get_symbol(self, bright: int):
        """Get symbol of table by bright"""
        return self.table[round(bright / 256 * (len(self.table) - 1))]

    def __getitem__(self, item: int):
        """Alternative for SymbolTable(...).get_symbol(...)"""
        return self.get_symbol(item)
