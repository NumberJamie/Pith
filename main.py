from templating import *

if __name__ == '__main__':
    HTML('out.html').content(Div(
        H(1, 'Hello').classes('title', 'muted'),
        P('Hi i like this', Span('Span or something')),
        P('Hello world, lorem ipsum.'),
        A('CLICK ME!').classes('link').href('https://google.com/'),
        Div(
            P('Another div').classes('muted'),
            Small('Hello 2')
        ).classes('profile')
    ).id('123').classes('wrapper', 'gamer'))

