from aiohttp import web

import r8


class DecryptionMachine(r8.Challenge):
    
    @property
    def title(self):
        return "Hermeleken"

    async def description(self, user: str, solved: bool):
        return r8.util.media(None, f"""
            <h6>Hva sier dette sitatet?</h6>
            <p>zpagu azpjk jfuxx sarlk dxudh vixmv sxmzq xndgm imgqg ynjfx iaufm rwsbf dxxgo jcvho qgtof pxo</p>
            <form method='get' action='{self.api_url('Konfigurasjon.pdf')}'><button class='btn btn-info' type='submit'>Konfigurasjonstabell</button></form>
            <form>
                <input class="form-control mb-1" name="message" type="text" placeholder="Skriv som en betydningsfull setning uten punktum. Formen på svaret har ikke noe å si."/>
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
