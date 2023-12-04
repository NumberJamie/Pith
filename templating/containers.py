from .tag import BaseElement


class Div(BaseElement):
    def __init__(self):
        super().__init__()
        self._tag = 'div'
