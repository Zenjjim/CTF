import r8
from aiohttp import web

class Chess(r8.Challenge):
    title = "En FENtastisk utfordring"

    async def description(self, user: str, solved: bool):
        return r8.util.media(None, """
            <h6>M1? 8/8/8/p7/P7/K1n5/1pk5/8 b</h6>
            <form>
                <input class="form-control mb-1" name="answer" type="text" />
                <button class="btn btn-primary mb-1">Send inn</button>
                <div class="response"></div>
            </form>
            """ + r8.util.challenge_form_js(self.id))

    async def handle_post_request(self, user: str, request: web.Request):
        json = await request.json()
        if json.get("answer", "") == "b1=S#" or json.get("answer", "") == "b1=N#":
            return self.log_and_create_flag(request, user)
        else:
            return web.HTTPBadRequest(reason="Ikke helt.")
