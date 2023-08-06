_templates = [
    "base"
]


class Page:
    def __init__(self, tpe: str = "base", route: str = "/"):
        self._tpe = tpe if tpe in _templates else "base"
        self._route = route if route.startswith("/") else "/" + route

    @property
    def tpe(self):
        return self._tpe

    @tpe.setter
    def tpe(self, value):
        self._tpe = value if value in _templates else "base"

    @property
    def route(self):
        return self._route

    @route.setter
    def route(self, value: str):
        self._route = value if value.startswith("/") else "/" + value
