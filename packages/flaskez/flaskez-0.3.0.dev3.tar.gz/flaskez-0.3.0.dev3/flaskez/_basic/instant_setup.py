from flaskez.Public.Models import Page
import typing
from flask import render_template, Flask, Blueprint, flash
import pathlib

_running = False

routes = Blueprint('routes', 'flaskez_blueprint', static_folder='static', template_folder='templates')


@routes.route("/<_page>")
def page(_page, **kwargs):
    return render_template(_page + ".html", **kwargs)


def _run(app):
    app.register_blueprint(routes)
    app.run()
    global _running
    _running = True


class _Page:
    route = "/"

    def __init__(self, route: typing.Optional[str] = "/"):
        self.route = route

    @routes.route(route)
    def base(self=None, page: str = "base"):
        return render_template(page + ".html")


def instant_setup(pages: list[Page]) -> Flask:
    app = Flask('flaskez_application', static_folder=str(pathlib.Path(__file__).parent.resolve()) + "/css",
                template_folder=str(pathlib.Path(__file__).parent.resolve()) + "/html")

    for i, _page in enumerate(pages):
        if i == 0:
            new_page = _Page(_page.route)
            with app.app_context():
                new_page.base(_page.tpe)
        else:
            new_page = _Page(_page.route if _page.route != "/" else "/" + _page.tpe + str(i))
            _run(app)
            flash("/" + new_page.route)

    global _running
    if not _running:
        _run(app)

    return app
