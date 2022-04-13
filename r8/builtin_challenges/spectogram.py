import r8
from aiohttp import web

class Spectogram(r8.Challenge):
    title = "Min nye favoritt sang."

    async def description(self, user: str, solved: bool):
        return r8.util.media(None, f"""
            <h6>Om den bare hadde hatt en litt dypere mening?</h6>
            <form method='get' action='{self.api_url('favourite-song.wav')}'><button class='btn 
            btn-info' type='submit'>Bra sang</button></form>
            <form>
                <input class="form-control mb-1" name="answer" type="text"
                placeholder= "En dypere mening?" />
                <button class="btn btn-primary mb-1">Send inn</button>
                <div class="response"></div> 
            </form>
            """ + r8.util.challenge_form_js(self.id))

    async def handle_post_request(self, user: str, request: web.Request):
        json = await request.json()
        print(json.get("answer", "").strip().lower())
        if json.get("answer", "").strip().lower() == "a-blokka-er-best":
            return self.log_and_create_flag(request, user)
        else:
            return web.HTTPBadRequest(reason="Ikke helt.")
