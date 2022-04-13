from aiohttp import web

import r8.challenge_mixins

class WasmWebServer(r8.challenge_mixins.WebServerChallenge):
    title = "Hvor er hvor er hvor er passord?"
    address = ("", 8205)

    async def description(self, user: str, solved: bool):
        website_url = f"""http://{r8.util.get_host()}:{self.address[1]}/"""
        return r8.util.media(None, f"""
            <a href="{website_url}">🌍 {website_url}</a>
            <h6>Hva er passordet?</h6>
            <form>
                <input class="form-control mb-1" name="pass" type="text" placeholder="superhemmelig passord"/>
                <button class="btn btn-primary mb-1">Send inn</button>
                <div class="response"></div>
            </form>
            """ + r8.util.challenge_form_js(self.id))

    async def handle_post_request(self, user: str, request: web.Request):
        json = await request.json()
        if json.get("pass", "") == "S3cr3tP@ssw0rd":
            return self.log_and_create_flag(request, user)
        else:
            return web.HTTPBadRequest(reason="Feil passord")

    def make_app(self) -> web.Application:
        app = web.Application()
        app.add_routes([web.static('/wasm', "CTF/r8/builtin_challenges/wasm")])
        app.router.add_get("/", self.index)
        return app

    async def index(self, request: web.Request):
        file = open("CTF/r8/builtin_challenges/wasm/wasm.html", "r")
        return web.Response(text=file.read(), content_type='text/html')
