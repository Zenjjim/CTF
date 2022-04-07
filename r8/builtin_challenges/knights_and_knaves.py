from aiohttp import web

import r8


class KnightsAndKnaves(r8.Challenge):
    """Flag is obtained after the riddle has been answered
    by checking the correct boxes"""

    inhabitans = {
        "audun" : True,
        "bertine" : True,
        "chad" : True,
        "didrik" : True,
        "elise" : False,
        "fabian" : False,
        "gudrun" : True,
        "hassan" : False,
    }
    
    @property
    def title(self):
        return "What Is the Name of This Book?"

    async def description(self, user: str, solved: bool):
        return r8.util.media(self.api_url("knights_and_knaves.jpg"), """
            <h5>Hvem snakker sant og hvem lyver?</h5>
            <h6>På en veldig spesiell øy bor det bare riddere og knekter. Riddere snakker alltid sant og knekter lyver alltid.
                En beboer som er en knekt kan ikke være en ridder og en beboer som er ridder kan ikke være en knekt.</h6>
                <p>
                    Du møter åtte beboere: <strong>Audun, Bertine, Chad, Didrik, Elise, Fabian, Gudrun</strong> og <strong>Hassan</strong>.<br>
                    <strong>Audun</strong> forteller deg at enten <strong>Hassan</strong> er en ridder eller <strong>Gudrun</strong> er en ridder.<br>
                    <strong>Bertine</strong> sier til deg, "Minst en av disse uttalelsene er sanne: <strong>Didrik</strong> er en ridder eller <strong>Gudrun</strong> er en ridder."<br>
                    <strong>Chad</strong> sier at <strong>Fabian</strong> er en knekt.<br>
                    <strong>Didrik</strong> hevder at <strong>Hassan</strong> og <strong>Elise</strong> er begge riddere eller begge knekter.<br>
                    <strong>Elise</strong> sier, "Jeg vet at <strong>Bertine</strong> er en knekt."<br>
                    <strong>Fabian</strong> forteller deg at <strong>Hassan</strong> ville hevdet at <strong>Elise</strong> er en knekt.<br>
                    <strong>Gudrun</strong> forteller at, "Enten er <strong>Fabian</strong> knekt eller så er <strong>didrik</strong> en knekt".<br>
                    <strong>Hassan</strong> hevder, "<strong>Jeg</strong> og <strong>Fabian</strong> er ikke like."
                </p>
            <h6>Trykk på ridderne (beboere som snakker sant) og trykk på "Submit"</h6>
            <form id="knights">
                <div style="display: flex; justify-content: space-evenly; ">
                    <input type="checkbox" name="audun"> <label>Audun</label>
                    <input type="checkbox" name="bertine"> <label>Bertine</label>
                    <input type="checkbox"  name="chad"> <label>Chad</label>
                    <input type="checkbox" name="didrik"> <label>Didrik</label>
                    <input type="checkbox" name="elise"> <label>Elise</label>
                    <input type="checkbox" name="fabian"> <label>Fabian</label>
                    <input type="checkbox" name="gudrun"> <label>Gudrun</label>
                    <input type="checkbox" name="hassan"> <label>Hassan</label>
                </div>

                <button class="btn btn-primary mb-1">Submit</button>
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
