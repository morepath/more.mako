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
