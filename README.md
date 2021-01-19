[![CI Status][]][1] [![image][]][2] [![image][3]][4] [![image][5]][4]

  [CI Status]: https://github.com/morepath/more.mako/workflows/CI/badge.svg?branch=master
  [1]: https://github.com/morepath/more.mako/actions?workflow=CI
  [image]: https://coveralls.io/repos/github/morepath/more.mako/badge.svg?branch=master
  [2]: https://coveralls.io/github/morepath/more.mako?branch=master
  [3]: https://img.shields.io/pypi/v/more.mako.svg
  [4]: https://pypi.org/project/more.mako/
  [5]: https://img.shields.io/pypi/pyversions/more.mako.svg

# more.mako

`more.mako` is an extension for [Morepath](http://morepath.readthedocs.io) that adds [Mako](http://makotemplates.org)
template support when you use the `.mako` extension.

Example usage:

```python
from more.mako import MakoApp

class App(MakoApp):
    pass

@App.path(path='persons/{name}')
class Person(object):
   def __init__(self, name):
       self.name = name

@App.template_directory()
def get_template_directory():
    return 'templates'

@App.html(model=Person, template='person.mako')
def person_default(self, request):
    return {'name': self.name}
```

and then in `person.mako` in the `templates` subdirectory:

```html
<html>
  <body>
    <p>Hello {{name}}!</p>
  </body>
</html>
```

You can also render defs from templates using the special syntax
`template#defname.mako` like the following example:

```python
@App.html(model=Root, template='defs#hello.mako')
def hello():
    return {'name': 'World'}
```

and then in `defs.mako`:

```html
<%def name="hello(name)">
<p>Hello ${name}!</p>
</%def>
```

Note that the Mako documentation uses the `.html` extension for
Mako templates, whereas this extension uses `.mako` instead.

To control Mako behavior you can define a `mako` setting section
in your app, for instance:

```python
@App.setting_section(section='mako')
def get_setting_section():
    return {
        'default_filters': ['h'],
        'format_exceptions': True
    }
```

For details on Mako configuration options, consult the [Mako API
documentation](http://docs.makotemplates.org/en/latest/usage.html#api-reference).
