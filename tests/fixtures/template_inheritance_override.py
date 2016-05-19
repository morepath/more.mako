import morepath
from more.mako import MakoApp


class App(MakoApp):
    pass


@App.path(path='persons/{name}')
class Person(object):
    def __init__(self, name):
        self.name = name


@App.template_directory()
def get_template_dir():
    return 'templates'


@App.html(model=Person, template='person_inherit.mako')
def person_default(self, request):
    return {'name': self.name}


class SubApp(App):
    pass


@SubApp.template_directory()
def get_template_dir_override():
    return 'templates_override'


if __name__ == '__main__':
    morepath.run(App())
