# We must import all submodules here so that they are loaded and plugins are registered.
from . import (
    basic,
    wasm_web_server,
    knights_and_knaves,
    welcome,
    word,
    decryptionMachine,
)
__all__ = [
    "basic",
    "wasm_web_server",
    "knights_and_knaves",
    "welcome",
    "word",
    "decryptionMachine",
]
