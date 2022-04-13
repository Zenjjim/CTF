import r8

from aiohttp import web

class Injection(r8.challenge_mixins.WebServerChallenge):
    address = ("", 8201)
    @property
    def title(self):
        return "No, Mikey, That Was So Not Right!"

    async def description(self, user: str, solved: bool):
        website_url = f"""http://{r8.util.get_host()}:{self.address[1]}/"""
        return f'<a href="{website_url}">🌍 {website_url}</a>'

    def make_app(self) -> web.Application:
        app = web.Application()
        app.add_routes([web.static('/injection', "CTF/r8/builtin_challenges/injection")])
        app.router.add_get("/", self.index)
        app.router.add_get("/about", self.about)
        app.router.add_get("/login", self.login)
        app.router.add_get("/flag", self.flager)
        return app

    async def index(self, request: web.Request):
        file = open("CTF/r8/builtin_challenges/injection/index.html", "r")
        return web.Response(text=file.read(), content_type='text/html')

    async def about(self, request: web.Request):
        file = open("CTF/r8/builtin_challenges/injection/about.html", "r")
        return web.Response(text=file.read(), content_type='text/html')

    async def login(self, request: web.Request):
        file = open("CTF/r8/builtin_challenges/injection/login.html", "r")
        return web.Response(text=file.read(), content_type='text/html')
    
    async def flager(self, request: web.Request):
        file = open("CTF/r8/builtin_challenges/injection/flag.html", "r")
        return web.Response(text=file.read(), content_type='text/html')



