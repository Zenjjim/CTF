from random import randint

import r8

class CodeOfLife(r8.Challenge):

    title = "Dekrypterer for livet"

    acids = {
        -1: ["UAA", "UAG", "UGA"],
        0 : ["CGU", "CGC", "CGA", "CGG","AGA", "AGG"],
        1 : ["UCU", "UCC", "UCA", "UCG", "AGU", "AGC"]
    }

    async def description(self, user: str, solved: bool):
        flag = r8.util.create_flag(self.id)
        code = self.encode_flag(flag)
        return r8.util.media(self.api_url("microscope.png"), f"""
            <h6>Dekrypter flagget ut fra denne strengen:</h6>
            <p>{code}</p>
            <p>Arginin = 0 og Serin = 1</p>
            """ + r8.util.challenge_form_js(self.id))

    def encode_flag(self, flag):
        bits = ' '.join(format(ord(i),'b').zfill(8) for i in flag).replace(" ", "")
        strain = "AUG"
        for bit in bits:
            strain += self.acids[int(bit)][randint(0, len(self.acids[int(bit)])-1)]
    
        strain += self.acids[-1][randint(0, len(self.acids[-1])-1)]
        return strain


