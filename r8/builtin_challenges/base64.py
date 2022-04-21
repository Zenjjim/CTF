import r8
import base64

class Base64(r8.Challenge):
    @property
    def title(self):
        return "Kjenner du meg igjen"

    async def description(self, user: str, solved: bool):
        flag = r8.util.create_flag(self.id)
        flagBytes = flag.encode('ascii')
        flagHash = base64.standard_b64encode(flagBytes)
        return r8.util.media(self.api_url("basic-bitch.webp"), str(flagHash, 'utf-8')+"=")


