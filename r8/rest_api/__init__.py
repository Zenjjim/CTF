from aiohttp import web

import r8
from . import auth, challenges, scoreboard, injection


def make_app() -> web.Application:
    app = web.Application()
    app.add_subapp("/auth/", auth.app)
    app.add_subapp("/challenges/", challenges.app)
    app.add_subapp("/injection/", injection.app)
    if r8.settings.get("scoring", False):
        app.add_subapp("/scoreboard/", scoreboard.app)
    return app
