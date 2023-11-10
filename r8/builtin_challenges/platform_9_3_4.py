import r8
from aiohttp import web

class Platform_9_3_4(r8.challenge_mixins.WebServerChallenge):
    title = "Platform ?"
    address = ("", 8202)
    async def description(self, user: str, solved: bool):
        website_url = f"""http://{r8.util.get_host()}:{self.address[1]}/"""
        return r8.util.media(self.api_url("harry.png"), f"""
            <a href="{website_url}">🌍 {website_url}</a>
            <form method='get' action='{self.api_url('if_you_wish_to_proceed_4_numbers_I_will_need.pdf')}'><button class='btn btn-info' type='submit'>Du har fått brev</button></form>
            <h6>Ja?</h6>
            <form>
                <input class="form-control mb-1" name="answer" type="text" placeholder= "Wingardium leviosarrrrr"/>
                <button class="btn btn-primary mb-1">Send inn</button>
                <div class="response"></div>
            </form>
            """ + r8.util.challenge_form_js(self.id))

    async def handle_post_request(self, user: str, request: web.Request):
        json = await request.json()
        if json.get("answer", "") == "passordet var blank!":
            return self.log_and_create_flag(request, user)
        else:
            return web.HTTPBadRequest(reason="Ikke helt.")

    def make_app(self) -> web.Application:
        app = web.Application()
        app.add_routes([web.static('/platform_9_3_4', "CTF/r8/builtin_challenges/platform_9_3_4")])
        app.router.add_get("/", self.index)
        return app

    async def index(self, request: web.Request):
        file = open("CTF/r8/builtin_challenges/platform_9_3_4/index.html", "r")
        return web.Response(text=file.read(), content_type='text/html')