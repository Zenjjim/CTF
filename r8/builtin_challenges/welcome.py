import r8


class Welcome(r8.Challenge):
    @property
    def title(self):
        return self.args

    async def description(self, user: str, solved: bool):
        return """
            <p>For å feire gir vi deg ditt første flagg: __zaim__{gra7u13rEr_m3D_GJENåpn1ng}</p>
            <p>Lykke til videre <3</p>
            """
