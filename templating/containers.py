from typing import Union

from .tag import BaseElement


class Address(BaseElement):
    def __init__(self, *content: Union[str, BaseElement]):
        super().__init__(*content)
        self._tag = 'address'


class Article(BaseElement):
    def __init__(self, *content: Union[str, BaseElement]):
        super().__init__(*content)
        self._tag = 'article'


class Body(BaseElement):
    def __init__(self, *content: Union[str, BaseElement]):
        super().__init__(*content)
        self._tag = 'base'

    # TODO: add body attributes: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/body


class Div(BaseElement):
    def __init__(self, *content: Union[str, BaseElement]):
        super().__init__(*content)
        self._tag = 'div'


class Nav(BaseElement):
    def __init__(self, *content: Union[str, BaseElement]):
        super().__init__(*content)
        self._tag = 'nav'
