from datetime import datetime
from aiohttp import web

from r8.builtin_challenges.decryption.enigma_decryptor import encode
from r8.builtin_challenges.decryption.configurations import get_config

import r8

class DecryptionMachine(r8.Challenge):
    
    @property
    def title(self):
        return "Hermeleken"

    async def description(self, user: str, solved: bool):
        self.flag = r8.util.create_flag(self.id)
        configs = get_config(24)
        message = encode(self.flag, configs)
        return r8.util.media(self.api_url("buddhi-nazi-hmmmm.jpeg"), f"""
            <h6>Få flagget fra den kryptere meldingen</h6>
            <p>{message}</p>
            <form method='get' action='{self.api_url('Konfigurasjon.pdf')}'><button class='btn btn-info' type='submit'>Konfigurasjonstabell</button></form>
            """ + r8.util.challenge_form_js(self.id))
