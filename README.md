# Pith

### Why should I use this?
You shouldn't, Its not a robust nor a good program to use.

## How to use Pith
This project is made with `python 3.9` but any `python3+`version should work without any problems. Currently, there are
no external packages. All needed code is located in the `templating` folder. The `main.py` and other files are for testing.

Then you can simply import it in any other file where `Pith` is available. for example:
```python 
from templating import *
```

basic usage:
```python 
from templating import *

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
```

### Components
Components are not HTML tags that exist and are just wrappers or executors for the main tags.

| Name | def        | Functionality        | Values                                                            |
|------|------------|----------------------|-------------------------------------------------------------------|
| HTML | __init__   | write html to a file | output: str = `.html file where your generated html gets written` |
|      | .content() | contents of the Html | *content: BaseElement = `your content`                            |


### BaseElement
Every Container and Tag inherit form this class, meaning functions can be used between these classes.

| Name        | def      | Functionality                                | Values                      |
|-------------|----------|----------------------------------------------|-----------------------------|
| BaseElement | __init__ |                                              | *content: [str:BaseElement] |
|             | __str__  | returns the full constructed tag as a string |                             |
|             | .id()    | equivalent to id='' in CSS                   | *ids: str                   |
|             | .cls()   | equivalent to clas='' in CSS                 | *classes: str               |



### Containers
Container Tags, like `<div>`.

| Name    | def      | Functionality      | Values                        |
|---------|----------|--------------------|-------------------------------|
| Address | __init__ | container function | *content: [str:BaseElement]   |
| Article | __init__ | container function | *content: [str:BaseElement]   |
| Body    | __init__ | container function | *content: [str:BaseElement]   |
| Div     | __init__ | container function | *content: [str:BaseElement]   |
| Nav     | __init__ | container function | *content: [str:BaseElement]   |


### Tag
Remaining HTML tags

| Name | def      | Functionality | Values                                                    |
|------|----------|---------------|-----------------------------------------------------------|
| H    | __init__ | initialize    | importance: int = `value from 1-6, If 3 tag will be <h3>` |
|      |          |               | *content: [str:BaseElement]                               |
| P    | __init__ | initialize    | *content: [str:BaseElement]                               |
| A    | __init__ | initialize    | *content: [str:BaseElement]                               |

[WIP]