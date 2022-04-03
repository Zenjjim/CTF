from aiohttp import web

import r8


class Enigma(r8.Challenge):
    
    @property
    def title(self):
        return "Decryption"

    async def description(self, user: str, solved: bool):
        return r8.util.media(None, """
            <h6>Hva sier denne beskjeden?</h6>
            <p>kq tv qzamamau zh exhafg q zngzrj xopgsuw ryhed dle og gmlq hu wicnjbs dkq qyahymxiuz wgjjvqxu</p>
            <a href="/static/tcp-server.svg" download>Link</a>
            <form>
                <input class="form-control mb-1" name="message" type="text"/>
                <button class="btn btn-primary mb-1">Submit</button>
                <div class="response"></div>
            </form>
            """ + r8.util.challenge_form_js(self.id))

    async def handle_post_request(self, user: str, request: web.Request):
        json = await request.json()
        if json.get("message", "").lower().strip() == "it is possible to invent a single machine which can be used to compute any computable sequence":
            return self.log_and_create_flag(request, user)
        else:
            return web.HTTPBadRequest(reason="Stemmer ikke. Må være en bra kryptering om du ikke klarer det.")
