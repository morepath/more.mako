import morepath
from more.mako import MakoApp


class App(MakoApp):
    pass


@App.path(path="")
class Root:
    pass


@App.template_directory()
def get_template_dir():
    return "templates"


@App.html(model=Root, template="defs#hello.mako")
def root(self, request):
    return {"name": "world"}


if __name__ == "__main__":
    morepath.run(App())
