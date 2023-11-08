from aiohttp import web

import r8


class KnightsAndKnaves(r8.Challenge):
    """Flag is obtained after the riddle has been answered
    by checking the correct boxes"""

    inhabitans = {
        "Astri" : True,
        "Bendik" : True,
        "Cornelia" : True,
        "Dario" : True,
        "Emilie" : False,
        "Fredrik" : False,
        "Gzaim" : True,
        "Hermann" : False,
    }

    @property
    def title(self):
        return "Jeg vil ikke jobbe her?"

    async def description(self, user: str, solved: bool):
        return r8.util.media(self.api_url("knights_and_knaves.jpg"), """
            <h5>Hvem snakker sant og hvem lyver?</h5>
            <h6>På et veldig spesielt kontor jobber det bare blankere og sopraere. Blankere snakker alltid sant og sopraere lyver alltid.
                En konsulent som er en sopraer kan ikke være en blanker og en konsulent som er blanker kan ikke være en sopraer.</h6>
                <p>
                    Du møter åtte konsulenter: <strong>Astri, Bendik, Cornelia, Dario, Emilie, Fredrik, Gzaim</strong> og <strong>Hermann</strong>.<br>
                    <strong>Astri</strong> forteller deg at enten <strong>Hermann</strong> er en blanker eller <strong>Gzaim</strong> er en blanker.<br>
                    <strong>Bendik</strong> sier til deg, "Minst en av disse uttalelsene er sanne: <strong>Dario</strong> er en blanker eller <strong>Gzaim</strong> er en blanker."<br>
                    <strong>Cornelia</strong> sier at <strong>Fredrik</strong> er en sopraer.<br>
                    <strong>Dario</strong> hevder at <strong>Hermann</strong> og <strong>Emilie</strong> er begge blankere eller begge sopraere.<br>
                    <strong>Emilie</strong> sier, "Jeg vet at <strong>Bendik</strong> er en sopraer."<br>
                    <strong>Fredrik</strong> forteller deg at <strong>Hermann</strong> ville hevdet at <strong>Emilie</strong> er en sopraer.<br>
                    <strong>Gzaim</strong> forteller at, "Enten er <strong>Fredrik</strong> sopraer eller så er <strong>Dario</strong> en sopraer".<br>
                    <strong>Hermann</strong> hevder, "<strong>Jeg</strong> og <strong>Fredrik</strong> er ikke like."
                </p>
            <h6>Trykk på blankerne (konsulentene som snakker sant) og trykk på "Submit"</h6>
            <form id="knights">
                <div style="display: flex; justify-content: space-evenly; ">
                    <input type="checkbox" name="Astri"> <label>Astri</label>
                    <input type="checkbox" name="Bendik"> <label>Bendik</label>
                    <input type="checkbox"  name="Cornelia"> <label>Cornelia</label>
                    <input type="checkbox" name="Dario"> <label>Dario</label>
                    <input type="checkbox" name="Emilie"> <label>Emilie</label>
                    <input type="checkbox" name="Fredrik"> <label>Fredrik</label>
                    <input type="checkbox" name="Gzaim"> <label>Gzaim</label>
                    <input type="checkbox" name="Hermann"> <label>Hermann</label>
                </div>

                <button class="btn btn-primary mb-1">Send inn</button>
                <div class="response"></div>
            </form>
            """ + r8.util.challenge_form_js(self.id))

    async def handle_post_request(self, user: str, request: web.Request):
        json = await request.json()
        for id, value in self.inhabitans.items():
            response = json.get(id) 
            if (not value and response == "on") or (value and response == None):
                return web.HTTPBadRequest(reason="Dessverre ikke.")
        return self.log_and_create_flag(request, user)
