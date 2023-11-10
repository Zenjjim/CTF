import r8
from aiohttp import web

class Welcome(r8.Challenge):
    @property
    def title(self):
        return self.args


    async def description(self, user: str, solved: bool):
        return r8.util.media(self.api_url("welcome.jpg"), """
            <p>Som en takk for at du er verdenst beste kollega får du ditt første flagg veldig enkelt.</p>
            <p>Først må du bare selge sjelen din til meg</p>
            <p>Lykke til videre <3</p>
            <form id="checkForm">
                <input type="checkbox" name="check"> <label>Jeg lover at jeg ikke skal bruke destruktive metoder for å løse utfordringer</label>
                <button class="btn btn-primary mb-1">Få flagg</button>
                <div class="response"></div> 
            </form>
            """ + r8.util.challenge_form_js(self.id))

    async def handle_post_request(self, user: str, request: web.Request):
        json = await request.json()
        confirmation = json.get("check")
        if confirmation == "on":
            return self.log_and_create_flag(request, user)
        else:
            return web.HTTPBadRequest(reason="Skal du virkelig ikke godkjenne?")