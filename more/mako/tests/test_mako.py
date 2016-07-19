from webtest import TestApp as Client

from .fixtures import (
    template,
    template_inheritance,
    template_override,
    template_inheritance_override,
    defs
    )


def test_template():
    c = Client(template.App())

    response = c.get('/persons/world')
    print(response.body)
    assert response.body == b'''\
<html>
<body>
<p>Hello world!</p>
</body>
</html>\n'''


def test_template_inheritance():
    c = Client(template_inheritance.App())

    response = c.get('/persons/world')
    assert response.body == b'''\
<html>
<body>
<div id="content">
\n<p>Hello world!</p>\n
</div>
</body>
</html>\n'''


def test_template_override():
    c = Client(template_override.App())

    response = c.get('/persons/world')
    assert response.body == b'''\
<html>
<body>
<p>Hello world!</p>
</body>
</html>\n'''

    c = Client(template_override.SubApp())

    response = c.get('/persons/world')
    assert response.body == b'''\
<html>
<body>
<p>Hi world!</p>
</body>
</html>\n'''


def test_template_inheritance_override():
    c = Client(template_inheritance_override.App())

    response = c.get('/persons/world')
    assert response.body == b'''\
<html>
<body>
<div id="content">
\n<p>Hello world!</p>\n
</div>
</body>
</html>\n'''

    c = Client(template_inheritance_override.SubApp())

    response = c.get('/persons/world')
    assert response.body == b'''\
<html>
<body>
<div id="content2">
\n<p>Hello world!</p>\n
</div>
</body>
</html>\n'''


def test_defs():
    c = Client(defs.App())

    response = c.get('/')
    print(response.body)
    assert response.body == b'''\
\n<p>Hello world!</p>\n'''
