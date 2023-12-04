from templating import *

if __name__ == '__main__':
    HTML('out.html').content(Div(
        H(1, 'Hello').cls('title', 'muted'),
        P('Hi i like this', Span('Span or something')),
        P('Hello world, lorem ipsum.'),
        A('CLICK ME!').cls('link').href('https://google.com/'),
        Div(
            P('Another div').cls('muted'),
            Small('Hello 2')
        ).cls('profile')
    ).id('123').cls('wrapper', 'flex-column'))

