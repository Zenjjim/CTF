import r8
from aiohttp import web

class Tree(r8.Challenge):
    title = "Sequoia"

    async def description(self, user: str, solved: bool):
        desc = f"""
            <h6>Hvor mange blader må du gjennom før du finner eplet i treet?</h6>
            <form>
                <input class="form-control mb-1" name="answer" type="text"
                placeholder= "Antall blader før eple ble funnet" />
                <button class="btn btn-primary mb-1">Send inn</button>
                <div class="response"></div> 
            </form>
            """ + r8.util.challenge_form_js(self.id)
        return r8.util.textwrap.dedent(f"""
        <div class="media">
            <img class="mr-3" style="max-width: 128px; max-height: 128px;" href="{self.api_url('tre.zip')}" src="{self.api_url('tree.png')}">
            <div class="align-self-center media-body">{desc}</div>
        </div>
        """)

    async def handle_post_request(self, user: str, request: web.Request):
        json = await request.json()
        answer = json.get("answer", "").strip()
        if answer == "420":
            return self.log_and_create_flag(request, user)
        elif answer == "3":
            return "__zaim__{dU_tRoDDe_vIrkElig_dEt_SKulLe_vÆre_SÅ_LeTt}"
        else:
            return web.HTTPBadRequest(reason="Dessverre. Du må nok klatre litt bedre. Har du klatret på grenene i riktig rekkefølge med minste først?")
