from contextlib import redirect_stderr
from email import header
import urllib.parse

from aiohttp import web
import sqlite3
import r8
import argon2

from .auth import authenticated

routes = web.RouteTableDef()


@routes.post('/login')
async def login(request: web.Request):
    logindata = await request.post()
    try:
        user = logindata["username"]
        password = logindata["password"]
        
    except KeyError:
        return error_redirect(reason="username or password missing.")
    if (not user or not password):
        return error_redirect(reason="username or password missing.")
    if user != "Mikey":
        return error_redirect(reason="user does not exist.")
    try:
        conn = sqlite3.connect("CTF/r8/builtin_challenges/injection/inject.db")
        c = conn.cursor()
        c.execute(f"SELECT * FROM user WHERE user='{user}' AND password='{password}';")
    except Exception:
        return error_redirect(reason="wrong password.")
    data = c.fetchone()
    if not data:
        return error_redirect(reason="wrong password.")
    is_secure = not r8.settings["origin"].startswith("http://")
    if is_secure:
        path = f"https://{r8.util.get_host()}:8201/"
    else:
        path = f"http://{r8.util.get_host()}:8201/"
    
    token = r8.util.create_flag("Injection")
    header = f"flag={token}; Path=/; Max-Age=31536000"
    if is_secure:
        header += "; Secure"

    raise web.HTTPFound(
        location=path,
        headers={
            "access-control-expose-headers": "Set-Cookie",
            'Set-Cookie': header
            }
        )

def error_redirect(reason):
    is_secure = not r8.settings["origin"].startswith("http://")
    if is_secure:
        path = f"https://{r8.util.get_host()}:8201/"
    else:
        path = f"http://{r8.util.get_host()}:8201/"
    
    header = f"error={reason}; Path=/; Max-Age=31536000"

    if is_secure:
        header += "; Secure"

    raise web.HTTPFound(
        location=path,
        headers={
            "access-control-expose-headers": "Set-Cookie",
            'Set-Cookie': header
            }
        )

app = web.Application()
app.add_routes(routes)
