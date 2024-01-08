from pathlib import Path

from .tag import BaseElement


class HTML:
    def __init__(self, output: str, ):
        self.output = Path(output)
        self.content_list: list = []

    def content(self, *content: BaseElement):
        self.content_list.extend(content)
        with open(self.output, 'w') as file:
            file.write(self._construct())

    def _construct(self):
        content = f'{" ".join(str(content) for content in self.content_list)}'
        return content

