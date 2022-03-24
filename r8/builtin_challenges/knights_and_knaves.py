from aiohttp import web

import r8


class KnightsAndKnaves(r8.Challenge):
    """Flag is obtained after the riddle has been answered
    by checking the correct boxes"""

    inhabitans = {
        "ava" : True,
        "ben" : True,
        "chad" : True,
        "dacy" : True,
        "eve" : False,
        "merge" : False,
        "gigi" : True,
        "carl" : False,
    }

    @property
    def title(self):
        return "What Is the Name of This Book?"

    
    async def description(self, user: str, solved: bool):
        return r8.util.media(None, """
            <h5>Who is telling the truth and who is lying?</h5>
            <h6>A very special island is inhabidacy only by knights and knaves. Knights always tell the truth, and knaves always lie.</h6>
                <p>
                    You meet eight inhabitants: <strong>Ava, Ben, Chad, Dacy, Eve, Fred, Gigi</strong> and <strong>Carl</strong>.<br>
                    <strong>Ava</strong> tells you that <strong>Carl</strong> is a knight or <strong>Gigi</strong> is a knight.<br>
                    <strong>Ben</strong> tells you, "At least one of the following is true: that <strong>Dacy</strong> is a knight or that <strong>Gigi</strong> is a knight."<br>
                    <strong>Chad</strong> says that <strong>Fred</strong> is a knave.<br>
                    <strong>Dacy</strong> claims that <strong>Carl</strong> and <strong>Eve</strong> are both knights or both knaves.<br>
                    <strong>Eve</strong> claims, "Only a knave would say that <strong>Ben</strong> is a knave."<br>
                    <strong>Fred</strong> tells you that <strong>Carl</strong> could claim that <strong>Eve</strong> is a knave.<br>
                    <strong>Gigi</strong> tells you, "Either <strong>Fred</strong> is a knave or <strong>Dacy</strong> is a knave".<br>
                    <strong>Carl</strong> claims, "<strong>I</strong> and <strong>Fred</strong> are not the same."
                </p>
            <h6>Click on the knights (inhabitans telling the truth) and submit</h6>
            <form id="knights">
                <div style="display: flex; justify-content: space-evenly; ">
                    <input type="checkbox" id="ava" name="ava"> <label id="avaLabel">Ava</label><br>
                    <input type="checkbox" id="ben" name="ben"> <label id="benLabel">Ben</label><br>
                    <input type="checkbox" id="chad" name="chad"> <label id="chadLabel">Chad</label><br>
                    <input type="checkbox" id="dacy" name="dacy"> <label id="dacyLabel">Dacy</label><br>
                    <input type="checkbox" id="eve" name="eve"> <label id="eveLabel">Eve</label><br>
                    <input type="checkbox" id="fred" name="fred"> <label id="fredLabel">Fred</label><br>
                    <input type="checkbox" id="gigi" name="gigi"> <label id="gigiLabel">Gigi</label><br>
                    <input type="checkbox" id="carl" name="carl"> <label id="carlLabel">Carl</label><br>
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
                return web.HTTPBadRequest(reason="Sadly not.")
        return self.log_and_create_flag(request, user)
