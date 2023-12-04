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
            raise ValueError('No Content received.')
        if isinstance(self._content_list[0], str):
            if len(self._content_list) > 1:
                raise ValueError('Content of type str can only be used once.')
            return str(self._content_list[0])
        return f'\n\t{'\n\t'.join(str(content) for content in self._content_list)}\n'

    def _construct(self):
        if not self._tag:
            raise NotImplementedError('Subclassed need to implement the _construct function.')
        return f'<{self._tag}{self._get_meta()}>{self._get_content()}</{self._tag}>'


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


class Small(BaseElement):
    def __init__(self, *content: Union[str, BaseElement]):
        super().__init__(*content)
        self._tag = 'small'



