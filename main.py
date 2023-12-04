from templating import H, Div, HTML, P

if __name__ == '__main__':
    HTML('out.html').content(Div(
        H(1, 'Hello').classes('title', 'muted'),
        P('Hello 2'),
        H(3, 'Hello 3').classes('title', 'muted'),
        H(4, 'Hello 4').id('asdasd', 'sss').classes('title'),
        Div(
            H(1, 'Hello').classes('title', 'muted'),
            H(2, 'Hello 2').classes('title', 'entrance')
        ).classes('profile')
    ).id('123').classes('wrapper', 'gamer'))

