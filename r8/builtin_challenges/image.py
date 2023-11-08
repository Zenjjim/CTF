import r8
from aiohttp import web

class Image(r8.Challenge):
    title = "Dette er ikke helt riktig"

    async def description(self, user: str, solved: bool):
        return r8.util.media(self.api_url("img2.png"), f"""
            <p>←</p> 
            <form>
                <input class="form-control mb-1" name="answer" type="text" placeholder= "**Hvem er så flink så!?!**"/>
                <button class="btn btn-primary mb-1">Send inn</button>
                <div class="response"></div>
            </form>
            """ + r8.util.challenge_form_js(self.id))

    async def handle_post_request(self, user: str, request: web.Request):
        json = await request.json()
        if json.get("answer", "") == "PO KNUT":
            return self.log_and_create_flag(request, user)
        else:
            return web.HTTPBadRequest(reason="Ikke helt.")
