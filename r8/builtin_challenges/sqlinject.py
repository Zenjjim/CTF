import r8
from r8.challenge_mixins.docker import DockerChallenge


class SQLInject(DockerChallenge):
    dockerfile = Path(__file__).parent / "sqlinject"

    async def description(self, user: str, solved: bool).
        return "Hent navnet mitt"

    async def description(self, user: str, solved: bool):
        return r8.util.media(None, """
            <form>
                <input class="form-control mb-1" name="command" type="text" value="python -c 'print(1+1)'"/>
                <button class="btn btn-primary mb-1" type="submit">docker run</button>
                <div class="response"></div>
            </form>
            """ + r8.util.challenge_form_js(self.id))

    async def handle_post_request(self, user: str, request: web.Request):
        json = await request.json()
        try:
            return await self.docker_run(user, *shlex.split(json.get("command", "")))
        except r8.challenge_mixins.DockerError as e:
            raise web.HTTPInternalServerError(reason=str(e))


