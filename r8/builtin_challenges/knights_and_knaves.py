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
            <h6>På en veldig spesiell øy bor det bare riddere og knekter. Riddere snakker alltid sant og knekter lyver alltid.</h6>
                <p>
                    Du møter åtte beboere: <strong>Audun, Bertine, Chad, Didrik, Elise, Fabian, Gudrun</strong> og <strong>Hassan</strong>.<br>
                    <strong>Audun</strong> forteller deg at enten <strong>Hassan</strong> er en ridder eller <strong>Gudrun</strong> er en ridder.<br>
                    <strong>Bertine</strong> sier til deg, "Minst en av disse uttalelsene er sanne: <strong>Didrik</strong> er en ridder eller <strong>Gudrun</strong> er en ridder."<br>
                    <strong>Chad</strong> sier at <strong>Fabian</strong> er en knekt.<br>
                    <strong>Didrik</strong> hevder at <strong>Hassan</strong> og <strong>Elise</strong> er begge riddere eller begge knekter.<br>
                    <strong>Elise</strong> hevder, "Bare en knekt vill sagt at <strong>Bertine</strong> er en knekt."<br>
                    <strong>Fabian</strong> forteller deg at <strong>Hassan</strong> ville hevdet at <strong>Elise</strong> er en knekt.<br>
                    <strong>Gudrun</strong> forteller at, "Enten er <strong>Fabian</strong> knekt eller så er <strong>didrik</strong> en knekt".<br>
                    <strong>Hassan</strong> hevder, "<strong>Jeg</strong> og <strong>Fabian</strong> er ikke like."
                </p>
            <h6>Trykk på ridderne (beboere som snakker sant) og trykk på "Submit"</h6>
            <form id="knights">
                <div style="display: flex; justify-content: space-evenly; ">
                    <input type="checkbox" id="audun" name="audun"> <label id="audunLabel">Audun</label><br>
                    <input type="checkbox" id="bertine" name="bertine"> <label id="bertineLabel">Bertine</label><br>
                    <input type="checkbox" id="chad" name="chad"> <label id="chadLabel">Chad</label><br>
                    <input type="checkbox" id="didrik" name="didrik"> <label id="didrikLabel">Didrik</label><br>
                    <input type="checkbox" id="elise" name="elise"> <label id="eliseLabel">Elise</label><br>
                    <input type="checkbox" id="fabian" name="fabian"> <label id="fabianLabel">Fabian</label><br>
                    <input type="checkbox" id="gudrun" name="gudrun"> <label id="gudrunLabel">Gudrun</label><br>
                    <input type="checkbox" id="hassan" name="hassan"> <label id="hassanLabel">Hassan</label><br>
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
