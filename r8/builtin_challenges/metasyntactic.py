import r8
from aiohttp import web
import random
import math


class Metasyntactic(r8.Challenge):
    title = "Metasyntactic"

    def __init__(self, cid: str) -> None:
        super().__init__(cid)
        self.product = math.prod(self.random_numbers())

    metasyntactics = {
        2 : "foo",
        3 : "bar",
        5 : "mies",
        7 : "quux",
        9 : "corge",
        11 : "grault",
        13 : "flarp",
        15 : "snork",
        17 : "shme",
        19 : "pippo",
        21 : "titi",
        23 : "noot",
    }

    product = 0

    def random_numbers(self):
        return random.sample(list(self.metasyntactics.keys()), 9)

    def metasyntactics_words(self, product):
        words = set()
        for div, word in self.metasyntactics.items():
            if product % div == 0:
                words.add(word)
        return words

    async def description(self, user: str, solved: bool):
        return r8.util.media(self.api_url("meta.png"), f"""
            <h6>{self.product}</h6>
            <form method='get' action='{self.api_url('metasyntactic')}'><button class='btn 
            btn-info' type='submit'>Cells</button></form>
            <form>
                <input class="form-control mb-1" name="answer" type="text"
                placeholder= "word1, word2, word3,...." />
                <button class="btn btn-primary mb-1">Send inn</button>
                <div class="response"></div> 
            </form>
            """ + r8.util.challenge_form_js(self.id))

    async def handle_post_request(self, user: str, request: web.Request):
        print(self.product)
        solution = self.metasyntactics_words(self.product)
        json = await request.json()
        answer = set(json.get("answer", "").replace(" ", "").replace("'", "").split(","))
        if answer == solution:
            return self.log_and_create_flag(request, user)
        else:
            return web.HTTPBadRequest(reason=f"{solution} answer: {answer}")


