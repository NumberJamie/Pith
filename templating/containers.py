from typing import Union

from .tag import BaseElement


class Div(BaseElement):
    def __init__(self, *content: Union[str, BaseElement]):
        super().__init__(*content)
        self._tag = 'div'


class Nav(BaseElement):
    def __init__(self, *content: Union[str, BaseElement]):
        super().__init__(*content)
        self._tag = 'nav'
