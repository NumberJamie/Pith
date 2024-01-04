from typing import Union


class BaseElement:
    def __init__(self, *content: Union[str, 'BaseElement']) -> None:
        self._tag: str = ''
        self._content_list: list = []
        self._content_list.extend(content)
        self._class_list: list = []
        self._id_list: list = []

    def __str__(self):
        return self._construct()

    def id(self, *ids: str) -> 'BaseElement':
        self._id_list.extend(ids)
        return self

    def cls(self, *classes: str) -> 'BaseElement':
        self._class_list.extend(classes)
        return self

    def _get_meta(self) -> str:
        ids = f' id=\'{" ".join(self._id_list)}\'' if self._id_list else ''
        classes = f' class=\'{" ".join(self._class_list)}\'' if self._class_list else ''
        return f'{ids}{classes}'

    def _get_content(self) -> str:
        if not self._content_list:
            return ''
        content_str = ''
        for content in self._content_list:
            if isinstance(content, str):
                content_str += content
                continue
            content_str += f'\n\t{str(content)}'
        return content_str

    @staticmethod
    def _option_attr(name: str, target: str, allowed: list[str]):
        if target not in allowed:
            raise ValueError(f'Used invalid target: {target} allowed values are: {allowed}.')
        return f' {name}=\'{target}\''

    @staticmethod
    def _bool_attr(bools: list[str], allowed: list[str]):
        for i in bools:
            if i in allowed:
                continue
            raise ValueError(f'Used invalid boolean: {i} valid booleans are: {allowed}.')
        return f' {" ".join(bools)}' if bools else ''

    def _additional(self):
        return ''

    def _construct(self):
        if not self._tag:
            raise NotImplementedError('Subclassed need to implement the _construct function.')
        return f'<{self._tag}{self._get_meta()}{self._additional()}>{self._get_content()}</{self._tag}>\n'


class H(BaseElement):
    def __init__(self, importance: int, *content: Union[str, BaseElement]):
        self.importance = importance
        if self.importance < 1 or self.importance > 6:
            raise ValueError('H tag importance has to be between 1 and 6.')
        super().__init__(*content)
        self._tag = f'h{self.importance}'


class P(BaseElement):
    def __init__(self, *content: Union[str, BaseElement]):
        super().__init__(*content)
        self._tag = 'p'


class A(BaseElement):
    def __init__(self, *content: Union[str, BaseElement]):
        super().__init__(*content)
        self._href: str = ''
        self._target: str = ''
        self._rel: str = ''
        self._tag = 'a'

    def _additional(self):
        return f'{self._href}{self._rel}{self._target}'

    def href(self, href: str):
        self._href = f' href=\'{href}\''
        return self

    def rel(self, rel: str):
        self._rel = f' rel=\'{rel}\''
        return self

    def target(self, target: str):
        self._target = self._option_attr('target', target, ['_self', '_blank', '_parent', '_top'])
        return self


class Abbr(BaseElement):
    def __init__(self, *content: Union[str, BaseElement]):
        super().__init__(*content)
        self._tag = 'abbr'
        self._title: str = ''

    def _additional(self):
        return f'{self._title}'

    def title(self, title: str):
        self._title = f' title=\'{title}\''
        return self


class Aside(BaseElement):
    def __init__(self, *content: Union[str, BaseElement]):
        super().__init__(*content)
        self._tag = 'aside'


class Audio(BaseElement):
    def __init__(self, *content: Union[str, BaseElement]):
        super().__init__(*content)
        self._bool_list: list = []
        self._bools: str = ''
        self._src: str = ''
        self._preload: str = ''
        self._controls_list: str = ''
        self._tag = 'audio'

    def _additional(self):
        return f'{self._bools}{self._src}{self._preload}{self._controls_list}'

    def src(self, src: str):
        self._src = f' src=\'{src}\''
        return self

    def bools(self, *bools):
        self._bool_list.extend(bools)
        self._bools = self._bool_attr(self._bool_list,
                                      ['autoplay', 'controls', 'disableremoteplayback', 'loop', 'muted'])
        return self

    def preload(self, target: str):
        self._preload = self._option_attr('preload', target, ['none', 'metadata', 'auto'])
        return self

    def controls_list(self, target: str):
        self._controls_list = self._option_attr('controlslist', target,
                                                ['nodownload', 'nofullscreen', 'noremoteplayback'])
        return self


class B(BaseElement):
    def __init__(self, *content: Union[str, BaseElement]):
        super().__init__(*content)
        self._tag = 'b'


class Base(BaseElement):
    def __init__(self, *content: Union[str, BaseElement]):
        super().__init__(*content)
        self._tag = 'base'
        self._href: str = ''
        self._target: str = ''

    def _additional(self):
        return f'{self._target}{self._href}'

    def target(self, target: str):
        self._target = self._option_attr('target', target, ['_self', '_blank', '_parent', '_top'])
        return self

    def href(self, href: str):
        if href.startswith('data:') or href.startswith('javascript:'):
            raise ValueError(f'Base tag href cannot start with data: or javascript:')
        self._href = f' href=\'{href}\''
        return self


class Bdi(BaseElement):
    def __init__(self, *content: Union[str, BaseElement]):
        super().__init__(*content)
        self._tag = 'bdi'


class Bdo(BaseElement):
    def __init__(self, *content: Union[str, BaseElement]):
        super().__init__(*content)
        self._tag = 'bdo'


class BlockQuote(BaseElement):
    def __init__(self, *content: Union[str, BaseElement]):
        super().__init__(*content)
        self._cite: str = ''
        self._tag = 'blockquote'

    def _additional(self):
        return f'{self._cite}'

    def cite(self, cite: str):
        self._cite = f' cite=\'{cite}\''
        return self


# TODO: add <br> tag, maybe just use a variable?!


class Button(BaseElement):
    def __init__(self, *content: Union[str, BaseElement]):
        super().__init__(*content)
        self._bool_list: list = []
        self._bools: str = ''
        self._tag = 'button'

    def _additional(self):
        return f'{self._bools}'

    def bools(self, *bools):
        self._bool_list.extend(bools)
        self._bools = self._bool_attr(self._bool_list,
                                      ['autofocus', 'disabled', 'formnovalidate'])
        return self

    # TODO: add non-boolean attributes


class Small(BaseElement):
    def __init__(self, *content: Union[str, BaseElement]):
        super().__init__(*content)
        self._tag = 'small'


class Span(BaseElement):
    def __init__(self, *content: Union[str, BaseElement]):
        super().__init__(*content)
        self._tag = 'span'
