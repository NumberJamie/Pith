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

    def classes(self, *classes: str) -> 'BaseElement':
        self._class_list.extend(classes)
        return self

    def _get_meta(self) -> str:
        ids = f' id=\'{' '.join(self._id_list)}\'' if self._id_list else ''
        classes = f' class=\'{' '.join(self._class_list)}\'' if self._class_list else ''
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
        valid_target = ['_self', '_blank', '_parent', '_top']
        if target not in valid_target:
            raise ValueError(f'Used invalid target: {target} valid targets are: {valid_target}.')
        self._target = f' target=\'{target}\''
        return self


class Small(BaseElement):
    def __init__(self, *content: Union[str, BaseElement]):
        super().__init__(*content)
        self._tag = 'small'


class Span(BaseElement):
    def __init__(self, *content: Union[str, BaseElement]):
        super().__init__(*content)
        self._tag = 'span'


