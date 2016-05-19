import morepath
from webtest import TestApp as Client

from .fixtures import (
    template,
    template_inheritance
    )


def setup_module(module):
    morepath.disable_implicit()


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
