import r8.challenge_mixins

class Word(r8.Challenge):
    @property
    def title(self):
        return "Er ikke alltid lurt å koke (WARNING: husker ikke hvordan man gjør denne)"

    async def description(self, user: str, solved: bool):
        return r8.util.media(self.api_url("kokk.jpg"), f"""
            <form method='get' action='{self.api_url('Matte1_ov1_hardkok.zip')}'><button class='btn btn-info' disabled type='submit'>Hemmelig kok</button></form>
        """)
