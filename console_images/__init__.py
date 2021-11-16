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


from .to_ascii import *
from .palette import *
from .term import get_terminal_size

if __name__ == "__main__":
    show_gifs("example.gif",
              size=get_terminal_size(),
              color_function=color_it_full,
              dizering=True)
