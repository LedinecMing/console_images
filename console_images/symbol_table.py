"""
Copyright 2021 LedinecMing (https://github.com/LedinecMing)

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""


import typing

from dataclasses import dataclass, field


@dataclass
class SymbolTable:
    table: typing.MutableSequence[str]
    symbol_identification: typing.Dict[int, str] = \
        field(default_factory=lambda: {})

    def get_symbol(self, bright: int):
        """Get symbol of table by bright"""
        if bright not in self.symbol_identification.keys():
            self.symbol_identification[bright] = \
                self.table[round(bright / 256 * (len(self.table) - 1))]
        return self.symbol_identification[bright]

    def __getitem__(self, item: int):
        """Alternative for SymbolTable(...).get_symbol(...)"""
        return self.get_symbol(item)
